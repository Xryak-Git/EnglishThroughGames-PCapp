from .db import BaseModel
from peewee import CharField, ForeignKeyField, TextField


class Users(BaseModel):
    name = CharField()


class Games(BaseModel):
    title = CharField()


class Videos(BaseModel):
    path = CharField()

    game_id = ForeignKeyField(Games, backref='games')
    user_id = ForeignKeyField(Users, backref='users')


class LearningWords(BaseModel):
    word_combination = CharField()

    user_id = ForeignKeyField(Users, backref='users')


class Images(BaseModel):
    title = CharField()
    text = TextField()
    path = CharField()
    path_boxes = CharField()

    game_id = ForeignKeyField(Games, backref='games')


class LearningWordsImages(BaseModel):
    learning_word_id = ForeignKeyField(LearningWords, backref='learning_words')
    image_id = ForeignKeyField(Images, backref='images')