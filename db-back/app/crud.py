from sqlalchemy.orm import Session

from . import models, schemas

#Users
def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    password = user.password
    db_user = models.Users(username=user.username, first_name=user.first_name, last_name=user.last_name, level=user.level, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user\

#Chords
def get_chord(db: Session, chord_id: int):
    return db.query(models.Chords).filter(models.Chords.id == chord_id).first()


def get_chords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Chords).offset(skip).limit(limit).all()


def create_chord(db: Session, chord: schemas.ChordCreate):
    name = chord.name
    db_chord = models.Users(name = name, barre=chord.barre, string1=chord.string1, string2=chord.string2, string3=chord.string3, string4=chord.string4,string5=chord.string5,string6=chord.string6,)
    db.add(db_chord)
    db.commit()
    db.refresh(db_chord)
    return db_chord

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item