from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, auth, notes
from app.db.mongo import init_mongo, close_mongo
from app.db.indexes import ensure_indexes

app = FastAPI(title="Notes API", version="1.0.0")

# CORS
import os
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await init_mongo()
    await ensure_indexes()

@app.on_event("shutdown")
async def on_shutdown():
    await close_mongo()

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])