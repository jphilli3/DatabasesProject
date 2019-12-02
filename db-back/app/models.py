from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.mysql import TINYINT 
from sqlalchemy.orm import relationship

from .database import Base


progression_chord_association = Table("In_Progression", Base.metadata,
    Column("ProgressionID",Integer,ForeignKey("Chord_Progression.id")),
    Column("ChordID",Integer, ForeignKey("chord.id")))

song_chord_association = Table("Uses_Chords", Base.metadata,
    Column("SongID",Integer,ForeignKey("songs.id")),
    Column("ChordID",Integer, ForeignKey("chord.id")))

song_progression_association = Table("In_Song", Base.metadata,
    Column("SongID",Integer,ForeignKey("songs.id")),
    Column("ProgressionID",Integer, ForeignKey("Chord_Progression.id")))

user_chord_assocociation = Table("Knows_Chord", Base.metadata,
    Column("UserID",Integer,ForeignKey("user.id")),
    Column("ChordID",Integer, ForeignKey("chord.id")))



class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String(55), unique=True, nullable=False)
    first_name = Column(String(55), nullable=False)
    last_name = Column(String(55), nullable=False)
    player_level = Column(Integer, nullable=False)
    password = Column(String(55), nullable=False)

    user_chords = relationship("Chord", secondary=user_chord_assocociation, back_populates="known_chords")



class Songs(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(110), nullable=False)
    artist = Column(String(110), nullable=False)
    difficulty = Column(Integer, nullable=False)

    chords_in = relationship("Chord", secondary=song_chord_association, back_populates="in_songs")
    progressions_in = relationship("Chord_Progression", secondary=song_progression_association, back_populates="progressions_in_songs")

class Chord(Base):
    __tablename__ = "chord"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    chord_name = Column(String(3),nullable=False)
    barre = Column(Boolean, nullable=False)
    barre_fret = Column(TINYINT(1), nullable = True)
    string6 = Column(TINYINT(1), nullable = True)
    string5 = Column(TINYINT(1), nullable = True)
    string4 = Column(TINYINT(1), nullable = True)
    string3 = Column(TINYINT(1), nullable = True)
    string2 = Column(TINYINT(1), nullable = True)
    string1 = Column(TINYINT(1), nullable = True)
    max_fret = Column(TINYINT(1), nullable = True)

    known_chords = relationship("User", secondary=user_chord_assocociation,back_populates="user_chords")
    in_songs = relationship("Songs",secondary=song_chord_association,back_populates="chords_in")
    progressions_with_chords= relationship("Chord_Progression",secondary=progression_chord_association,back_populates="chords_in_progression")

class Chord_Progression(Base):
    __tablename__ = "Chord_Progression"

    id = Column(Integer, primary_key=True, nullable=False)
    key_name = Column(String(3), nullable=False)

    chords_in_progression = relationship("Chord", secondary=progression_chord_association,back_populates="progressions_with_chords")
    progressions_in_songs = relationship("Songs",secondary=song_progression_association,back_populates="progressions_in")
