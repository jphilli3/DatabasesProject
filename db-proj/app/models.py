from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String(55), unique=True, index=True, nullable=False)
    first_name = Column(String(55), index=True, nullable=False)
    last_name = Column(String(55), index=True, nullable=False)
    level = Column(Integer,index=True, nullable=False)
    password = Column(String(55), nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)

    # items = relationship("Item", back_populates="owner")

class Knows_Chord(Base):
    __tablename__ = "knows_chord"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    chord_id = Column(Integer, ForeignKey("chords.id"), nullable=False)

    #owner = relationship("User", back_populates="items")

class Songs(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(110), index=True, nullable=False)
    artist = Column(String(110), index=True, nullable=False)
    difficulty = Column(Integer, index=True, nullable=False)

class Uses_Chords(Base):
    __tablename__ = "uses_chords"

    song_id = Column(Integer, ForeignKey("songs.id"), nullable=False)
    chord_id = Column(Integer, ForeignKey("chords.id"), nullable=False)

class Chords(Base):
    __tablename__ = "chords"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(3),nullable=False)
    barre = Column(Boolean, nullable=False)
    string1 = Column(Integer, nullable=False)
    string2 = Column(Integer, nullable=False)
    string3 = Column(Integer, nullable=False)
    string4 = Column(Integer, nullable=False)
    string5 = Column(Integer, nullable=False)
    string6 = Column(Integer, nullable=False)

class Chord_Progressions(Base):
    __tablename__ = "chord_progressions"

    id = Column(Integer, primary_key=True, nullable=False)
    key = Column(String(3), nullable=False)

class In_Song(Base):
    __tablename__ = "in_song"

    song_id = Column(Integer, ForeignKey("songs.id"), nullable=False)
    progression_id = Column(Integer, ForeignKey("chord_progressions.id"), nullable=False)

class In_Progression(Base):
    __tablename__ = "in_progression"

    progression_id = Column(Integer, ForeignKey("chord_progressions.id"), nullable=False)
    chord_id = Column(Integer, ForeignKey("chords.id"), nullable=False)