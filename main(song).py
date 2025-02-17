from typing import List
from fastapi import FastAPI, HTTPException
from database.schemas import SongCreate, SongUpdate, SongResponse
from database.base import session
from database.songs import Song

app = FastAPI()


@app.post("/songs/", response_model=SongResponse)
async def create_song(todo: SongCreate):
    db_song = Song(**todo.dict())
    session.add(db_song)
    session.commit()
    return db_song


@app.get("/todos/", response_model=List[SongResponse])
async def get_songs():
    all_songs = session.query(Song).all()
    return all_songs


@app.get("/songs/{song_name}", response_model=SongResponse)
async def get_song_by_name(song_id: int):
    song = session.query(Song).filter(Song.id == song_id).first()
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@app.put("/song/{song_id}/", response_model=SongResponse)
def update_song(song_id: int, song: SongUpdate):
    song_obj = session.query(Song).filter(Song.id == song_id).first()
    if not song_obj:
        raise HTTPException(status_code=404, detail="Song not found")
    for key, value in song.dict().items():
        setattr(song_obj, key, value)
    session.commit()
    session.refresh(song_obj)
    return song_obj


@app.delete("/song/{song_id}")
async def delete_song(song_id: int):
    song_obj = session.query(Song).filter(Song.id == song_id).first()
    if not song_obj:
        raise HTTPException(status_code=404, detail="Song not found")
    session.delete(song_obj)
    session.commit()
    return {"detail": "Song was deleted successfully"}



