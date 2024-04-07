from .db import db
from .models import (Users, Games, Videos,
                     LearningWords, Images, LearningWordsImages)

db.connect()
db.create_tables([Users, Games, Videos,
                  LearningWords, Images, LearningWordsImages])

__all__ = [
    "Users", "Games", "Videos", "db",
    "LearningWords", "Images", "LearningWordsImages",
]
