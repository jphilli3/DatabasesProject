from typing import List

from pydantic import BaseModel



'''CREATE TABLE User (
	UserID: INT(),
	UserName: VARCHAR(),
	FirstName: VARCHAR(),
	LastName: VARCHAR(),
	Level: INT(),
	PRIMARY KEY (UserID)
);'''

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    level: int

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    deleted: bool

    class Config:
        orm_mode = True

'''CREATE TABLE Chord (
	ChordID: INT(),
	ChordName: VARCHAR(3),
	Barre: BOOLEAN(),
	String1: TINYINT(),
	String2: TINYINT(),
	String3: TINYINT(),
	String4: TINYINT(),
	String5: TINYINT(),
	String6: TINYINT(),	
	PRIMARY KEY (ChordID)
);'''

class ChordBase(BaseModel):
    name: str
    barre: bool
    string1: int
    string2: int
    string3: int
    string4: int
    string5: int
    string6: int

class ChordCreate(ChordBase):
    pass

class Chord(ChordBase):
    id: int

    class Config:
        orm_mode = True

'''CREATE TABLE Songs();
	SongID: INT(),
	Title: VARCHAR(),
	Artist: VARCHAR(),
	Difficulty: INT(),
	PRIMARY KEY (SongID)
);'''

class SongBase(BaseModel):
    title: str
    artist: str
    difficulty: str

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int

    class Config:
        orm_mode = True

'''CREATE TABLE Chord_Progression(
	ProgressionID: INT(),
	Key: VARCHAR(3),
	PRIMARY KEY (progressionID)
);'''

class ProgressionBase(BaseModel):
    key: str

class ProgressionCreate(ProgressionBase):
    pass

class Progression(ProgressionBase):
    id: int

    class Config:
        orm_mode = True

'''CREATE TABLE Uses_Chords (
	SongID:INT(),
	ChordID: INT(),
	FOREIGN KEY (SongID), 
	REFERENCES Songs,
	FOREIGN KEY (ChordID), 
	REFERENCES Chord
);'''

class UsesChordBase(BaseModel):
    song_id: int
    chord_id: int

class UsesChordCreate(UsesChordBase):
    pass

class UsesChord(UsesChordBase):
    id: int

    class Config: 
        orm_mode = True

'''CREATE TABLE In_Song(
	SongID: INT(), 
	ProgressionID: INT(),
      FOREIGN KEY (SongID), 
	REFERENCES Songs,
	FOREIGN KEY (ProgressionID), 
	REFERENCES Chord_Progression
);'''

class InSongBase(BaseModel):
    song_id: int
    progression_id: int

class InSongCreate(InSongBase):
    pass

class InSong(InSongBase):
    id: int

    class Config: 
        orm_mode = True

'''CREATE TABLE In_Progression (
	ProgressionID: INT(),
	ChordID: INT(),
	FOREIGN KEY(ProgressionID),
	REFERENCES Chord_Progression,
      FOREIGN KEY(ChordID),
	REFERENCES Chord
);'''

class InProgressionBase(BaseModel):
    chord_id: int
    progression_id: int

class InProgressionCreate(InProgressionBase):
    pass

class InProgression(InProgressionBase):
    id: int

    class Config: 
        orm_mode = True

'''CREATE TABLE Knows_Chord(
      UserID: INT(),
      ChordID: INT(),
	FOREIGN KEY (UserID), 
	REFERENCES User,
	FOREIGN KEY (ChordID), 
	REFERENCES Chord 
);'''

class KnowsChordBase(BaseModel):
    user_id: int
    chord_id: int

class KnowsChordCreate(KnowsChordBase):
    pass

class KnowsChord(KnowsChordBase):
    id: int

    class Config: 
        orm_mode = True