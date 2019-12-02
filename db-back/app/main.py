from typing import List

from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Guitar Hero",
    description = "Learning the guitar made easy",
    version = "1.0")

# add your front end server here:
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def healthCheck():
    return {"status":"up"}

@app.get("/users/{id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return crud.create_user(db=db, user=user)

@app.get("/chord/{id}", response_model=schemas.Chord)
def read_chord(chord_id: int, db: Session = Depends(get_db)):
    db_chord = crud.get_chord(db=db, chord_id=chord_id)
    if db_chord is None:
        raise HTTPException(status_code=404, detail="Chord not found")
    return db_chord

@app.get("/chords/", response_model=schemas.Chord)
def create_chord(chord: schemas.ChordCreate, db: Session = Depends(get_db)):
    db_chord = crud.get_chord(db=db,chord_id=chord.id)
    if db_chord:
        raise HTTPException(status_code=400, detail="Chord already created")
    return crud.create_chord(db=db, chord=chord)

@app.get("/progressions/{id}", response_model=schemas.Progression)
def read_progression(progression_id: int, db: Session = Depends(get_db)):
    db_progression = crud.get_progression(db=db, progression_id=progression_id)
    if db_progression is None:
        raise HTTPException(status_code=404, detail="Progression not found")
    return db_progression

@app.get("/progressions/", response_model=schemas.Progression)
def create_progression(progression: schemas.ProgressionCreate, db: Session = Depends(get_db)):
    db_progression = crud.get_progression(db=db,progression_id=progression.id)
    if db_progression:
        raise HTTPException(status_code=400, detail="Progression already created")
    return crud.create_progression(db=db, progression=progression)

@app.get("/songs/{id}", response_model=schemas.Song)
def read_song(song_id: int, db: Session = Depends(get_db)):
    db_song = crud.get_song(db=db, song_id=song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song

@app.get("/songs/", response_model=schemas.Song)
def create_song(song: schemas.SongCreate, db: Session = Depends(get_db)):
    db_song= crud.get_song(db=db,song_id=song.id)
    if db_song:
        raise HTTPException(status_code=400, detail="Song already created")
    return crud.create_progression(db=db, progression=song)
