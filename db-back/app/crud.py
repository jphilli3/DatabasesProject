from sqlalchemy.orm import Session

from . import models, schemas

#Users
def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()

def get_users_by_first_name(db: Session, first_name: str):
    return db.query(models.Users).filter(models.Users.first_name == first_name).all()

def get_users_by_last_name(db: Session, last_name: str):
    return db.query(models.Users).filter(models.Users.last_name == last_name).all()

def get_chords_user_knows(db: Session, user_id: str):
    return db.query(models.Knows_Chord).filter(models.Knows_Chord.user_id == user_id).all()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    password = user.password
    db_user = models.Users(username=user.username, first_name=user.first_name, last_name=user.last_name, level=user.level, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Chords
def get_chord(db: Session, chord_id: int):
    return db.query(models.Chords).filter(models.Chords.id == chord_id).first()

def get_chord_by_name(db: Session, chord_name: str):
    return db.query(models.Chords).filter(models.Chords.name == chord_name).first()

def get_chords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Chords).offset(skip).limit(limit).all()

def get_songs_with_chord(db: Session, chord_id: int):
    return db.query(models.Uses_Chords).filter(models.Uses_Chords.chord_id == chord_id).all()

def get_progression_with_chord(db: Session, chord_id: int):
    return db.query(models.In_Progression).filter(models.In_Progression.chord_id == chord_id).all()

def get_uses_that_know_chord(db: Session, chord_id: int):
    return db.query(models.Knows_Chord).filter(models.Knows_Chord.chord_id == chord_id).all()

def create_chord(db: Session, chord: schemas.ChordCreate):
    db_chord = models.Chords(name=chord.name, barre=chord.barre, string1=chord.string1, string2=chord.string2, string3=chord.string3, string4=chord.string4,string5=chord.string5,string6=chord.string6)
    db.add(db_chord)
    db.commit()
    db.refresh(db_chord)
    return db_chord

#Progressions
def get_progression(db: Session, progression_id: int):
    return db.query(models.Progressions).filter(models.Progressions.id == progression_id).first()

def get_progression_by_key(db: Session, progression_name: str):
    return db.query(models.Progressions).filter(models.Progressions.key == progression_name).first()

def get_progressions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Progressions).offset(skip).limit(limit).all()

def get_songs_with_progression(db: Session, progression_id: int):
    return db.query(models.In_Song).filter(models.In_Song.progression_id == progression_id).all()

def get_chords_in_progression(db: Session, progression_id: int):
    return db.query(models.In_Progression).filter(models.In_Progression.progression_id == progression_id).all()

def create_progression(db: Session, progression: schemas.ProgressionCreate):
    db_progression = models.Progressions(key=progression.key)
    db.add(db_progression)
    db.commit()
    db.refresh(db_progression)
    return db_progression

#Songs
def get_song(db: Session, song_id: int):
    return db.query(models.Songs).filter(models.Songs.id == song_id).first()

def get_song_by_title(db: Session, song_title: str):
    return db.query(models.Songs).filter(models.Songs.title == song_title).first()

def get_songs_by_artist(db: Session, artist: str):
    return db.query(models.Songs).filter(models.Songs.artist == artist).all()

def get_songs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Songs).offset(skip).limit(limit).all()

def get_chords_in_song(db: Session, song_id: int):
    return db.query(models.Uses_Chords).filter(models.Uses_Chords.song_id == song_id).all()

def get_progressions_in_song(db: Session, song_id: int):
    return db.query(models.In_Song).filter(models.In_Song.song_id == song_id).all()

def create_song(db: Session, song: schemas.SongCreate):
    db_song = models.Songs(title = song.title, artist = song.artist, difficulty = song.difficulty)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item