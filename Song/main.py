from typing import List
from fastapi import FastAPI, HTTPException
from Song.schemas import SongCreate, SongUpdate, SongResponse
from database.base import session
from Song.models import Song



app = FastAPI()



@app.post("/songs/", response_model=SongResponse)
async def create_song(song: SongCreate):
    db_song = Song(**song.dict())
    session.add(db_song)
    session.commit()
    return db_song


@app.get("/songs/", response_model=List[SongResponse])
async def get_songs():
    all_songs = session.query(Song).all()
    return all_songs


@app.get("/songs/{song_name}/", response_model=SongResponse)
async def get_song_by_name(song_name: str):
    song = session.query(Song).filter(Song.name == song_name).first()
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@app.put("/song/{song_name}/", response_model=SongResponse)
def update_song(song_name: str, song: SongUpdate):
    song_obj = session.query(Song).filter(Song.name == song_name).first()
    if not song_obj:
        raise HTTPException(status_code=404, detail="Song not found")
    for key, value in song.dict().items():
        setattr(song_obj, key, value)
    session.commit()
    session.refresh(song_obj)
    response = SongResponse(id=song_obj.id, name=song_obj.name, text=song_obj.text)
    return response


@app.delete("/song/{song_name}/")
async def delete_song(song_name: str):
    song_obj = session.query(Song).filter(Song.name == song_name).first()
    if not song_obj:
        raise HTTPException(status_code=404, detail="Song not found")
    session.delete(song_obj)
    session.commit()
    return {"detail": "Song was deleted successfully"}



