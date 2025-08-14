from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin, TokenOut
from app.core.security import hash_password, verify_password, create_access_token
from app.db.mongo import get_db
from uuid import uuid4
from datetime import datetime, timezone

router = APIRouter()

@router.post("/register", response_model=TokenOut)
async def register(payload: UserCreate):
    db = get_db()
    existed = await db.users.find_one({"user_email": payload.user_email})
    if existed:
        raise HTTPException(status_code=400, detail="Email already registered")
    now = datetime.now(timezone.utc).isoformat()
    user_id = str(uuid4())
    await db.users.insert_one({
        "user_id": user_id,
        "user_name": payload.user_name,
        "user_email": payload.user_email,
        "password": hash_password(payload.password),
        "created_on": now,
        "last_update": now,
    })
    token = create_access_token(user_id)
    return {"access_token": token}

@router.post("/login", response_model=TokenOut)
async def login(payload: UserLogin):
    db = get_db()
    user = await db.users.find_one({"user_email": payload.user_email})
    if not user or not verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(user["user_id"])
    return {"access_token": token}