from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.dialects.mysql import TINYINT 
from sqlalchemy.orm import relationship

from .database import Base


progression_chord_association = Table("In_Progression", Base.metadata,
    Column("ProgressionID",Integer,ForeignKey("Chord_Progression.id")),
    Column("ChordID",Integer, ForeignKey("Chord.id")))

song_chord_association = Table("Uses_Chords", Base.metadata,
    Column("SongID",Integer,ForeignKey("Songs.id")),
    Column("ChordID",Integer, ForeignKey("Chord.id")))

song_progression_association = Table("In_Song", Base.metadata,
    Column("SongID",Integer,ForeignKey("Songs.id")),
    Column("ProgressionID",Integer, ForeignKey("Chord_Progression.id")))

user_chord_assocociation = Table("Knows_Chord", Base.metadata,
    Column("UserID",Integer,ForeignKey("User.id")),
    Column("ChordID",Integer, ForeignKey("Chord.id")))

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True,)
    username = Column(String(30))
    password = Column(String(30))
    first_name = Column(String(30))
    last_name = Column(String(30))
    player_level = Column(Integer)

    known_chords = relationship("Chord", secondary=user_chord_assocociation, back_populates="User")

class Songs(Base):
    __tablename__ = "Songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    artist = Column(String(20))
    difficulty = Column(Integer)

    chords_in = relationship("Chord",secondary=song_chord_association,back_populates="Songs")
    progressions_in = relationship("Chord_Progression", secondary=song_progression_association,back_populates="Songs")

class Chord(Base):
    __tablename__ = "Chord"

    id = Column(Integer, primary_key=True, index = True)
    chord_name = Column(String(7))
    barre = Column(bool, nullable = True )
    barre_fret = Column(TINYINT(1), nullable = True)
    string6 = Column(TINYINT(1), nullable = True)
    string5 = Column(TINYINT(1), nullable = True)
    string4 = Column(TINYINT(1), nullable = True)
    string3 = Column(TINYINT(1), nullable = True)
    string2 = Column(TINYINT(1), nullable = True)
    string1 = Column(TINYINT(1), nullable = True)

    in_songs = relationship("Songs", secondary=song_chord_association,back_populates="Chord")
    in_progression = relationship("Chord_Progression",secondary=progression_chord_association ,back_populates="Chord")
    known_by = relationship("User",secondary=user_chord_assocociation,back_populates="Chord")

class Chord_Progression(Base):
    __tablename__ = "Chord_Progression"

    id = Column(Integer, primary_key=True,index=True)
    key_name = Column(String(3), nullable = True)

    progression_chords = relationship("Chord", secondary=progression_chord_association, back_populates="Chord_Progression")
    songs_with_progression = relationship("Songs", secondary=song_progression_association,back_populates="Chord_Progression")
    


