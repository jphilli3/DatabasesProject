from typing import List

from pydantic import BaseModel

##         CHORDS

class ChordBase(BaseModel):
    chord_name: str

class ChordCreate(ChordBase):
    pass 

class Chord(ChordBase):
    id: int
    barre: bool
    barre_fret: int
    string6: int
    string5: int
    string4: int 
    string3: int 
    string2: int
    string1: int 

    class Config:
        orm_mode = True

## CHORD PROGRESSIONS


class Chord_ProgressionBase(BaseModel):
    key_name:str

class Chord_ProgressionCreate(Chord_ProgressionBase):
    pass

class Chord_Progression(Chord_ProgressionBase):
    id: int
    
    progression_chords: List[Chord] = []

    class Config:
        orm_mode = True


## SONGS 

class SongsBase(BaseModel):
    title:str

class SongsCreate(SongsBase):
    pass

class Songs(SongsBase):
    id: int
    artist: str
    difficulty: int

    chords_in: List[Chord] = []
    progressions_in: List[Chord_Progression]=[]

    class Config:
        orm_mode=True

 ## USERS   

class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    first_name: str
    last_name: str 


class User(UserBase):
    id: int
    player_level: int
    known_chords: List[Chord] = []

    class Config:
        orm_mode = True

