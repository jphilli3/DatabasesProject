from typing import List

from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: str = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


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
    # items: List[Item] = []

    class Config:
        orm_mode = True

class ChordBase(BaseModel):
    name = str

class ChordCreate(ChordBase):
    barre = bool
    string1 = int
    string2 = int
    string3 = int
    string4 = int
    string5 = int
    string6 = int

class Chord(ChordBase):
    id: int

    class Config:
        orm_mode = True