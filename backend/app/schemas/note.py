from pydantic import BaseModel, Field
from typing import Optional

class NoteCreate(BaseModel):
    note_title: str = Field(min_length=1, max_length=200)
    note_content: str = ""  # HTML/Markdown string

class NoteUpdate(BaseModel):
    note_title: Optional[str] = None
    note_content: Optional[str] = None

class NoteOut(BaseModel):
    note_id: str
    note_title: str
    note_content: str
    user_id: str
    created_on: str
    last_update: str