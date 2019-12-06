from typing import List

from pydantic import BaseModel

class ChordBase(BaseModel):
    chord_name: str
    barre: bool
    barre_fret: int
    string1: int
    string2: int
    string3: int
    string4: int
    string5: int
    string6: int
    max_fret: int

class ChordCreate(ChordBase):
    pass

class Chord(ChordBase):
    id: int

    class Config:
        orm_mode = True


class ProgressionBase(BaseModel):
    key_name: str

class ProgressionCreate(ProgressionBase):
    pass

class Progression(ProgressionBase):
    id: int
    chords_in: List[Chord] = []

    class Config:
        orm_mode = True


class SongBase(BaseModel):
    title: str
    artist: str
    difficulty: str

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int
    chords_in: List[Chord] =[]
    progressions_in:List[Progression] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    level: int

class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    
    knows_chords: List[Chord] = []
    
    class Config:
        orm_mode = True