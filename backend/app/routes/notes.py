from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from uuid import uuid4
from datetime import datetime, timezone
from app.core.security import get_current_user
from app.db.mongo import get_db
from app.schemas.note import NoteCreate, NoteUpdate, NoteOut

router = APIRouter()

@router.get("/", response_model=List[NoteOut])
async def list_notes(skip: int = 0, limit: int = Query(20, le=100), user=Depends(get_current_user)):
    db = get_db()
    cur = db.notes.find({"user_id": user["user_id"]}).sort("created_on", -1).skip(skip).limit(limit)
    results = []
    async for n in cur:
        results.append({
            "note_id": n["note_id"],
            "note_title": n["note_title"],
            "note_content": n.get("note_content",""),
            "user_id": n["user_id"],
            "created_on": n["created_on"],
            "last_update": n["last_update"],
        })
    return results

@router.post("/", response_model=NoteOut)
async def create_note(body: NoteCreate, user=Depends(get_current_user)):
    db = get_db()
    now = datetime.now(timezone.utc).isoformat()
    note_id = str(uuid4())
    doc = {
        "note_id": note_id,
        "user_id": user["user_id"],
        "note_title": body.note_title,
        "note_content": body.note_content,
        "created_on": now,
        "last_update": now,
    }
    await db.notes.insert_one(doc)
    doc["user_id"] = user["user_id"]
    return doc

@router.get("/{note_id}", response_model=NoteOut)
async def get_note(note_id: str, user=Depends(get_current_user)):
    db = get_db()
    n = await db.notes.find_one({"note_id": note_id, "user_id": user["user_id"]})
    if not n:
        raise HTTPException(status_code=404, detail="Not found")
    return {
        "note_id": n["note_id"],
        "note_title": n["note_title"],
        "note_content": n.get("note_content",""),
        "user_id": n["user_id"],
        "created_on": n["created_on"],
        "last_update": n["last_update"],
    }

@router.put("/{note_id}", response_model=NoteOut)
async def update_note(note_id: str, body: NoteUpdate, user=Depends(get_current_user)):
    db = get_db()
    updates = {k: v for k, v in body.dict().items() if v is not None}
    if not updates:
        raise HTTPException(status_code=400, detail="No updates")
    updates["last_update"] = datetime.now(timezone.utc).isoformat()
    res = await db.notes.find_one_and_update(
        {"note_id": note_id, "user_id": user["user_id"]},
        {"$set": updates},
        return_document=True,
    )
    if not res:
        raise HTTPException(status_code=404, detail="Not found")
    res = await db.notes.find_one({"note_id": note_id})
    return {
        "note_id": res["note_id"],
        "note_title": res["note_title"],
        "note_content": res.get("note_content",""),
        "user_id": res["user_id"],
        "created_on": res["created_on"],
        "last_update": res["last_update"],
    }

@router.delete("/{note_id}")
async def delete_note(note_id: str, user=Depends(get_current_user)):
    db = get_db()
    r = await db.notes.delete_one({"note_id": note_id, "user_id": user["user_id"]})
    if r.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return {"deleted": True}