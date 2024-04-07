from peewee import Model
from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase('gamelearning.db', pragmas=(
    ('cache_size', -1024 * 64),  # 64MB page-cache.
    ('journal_mode', 'wal'),  # Use WAL-mode (you should always use this!).
    ('foreign_keys', 3)),  # Enforce foreign-key constraints.
)


class BaseModel(Model):
    class Meta:
        database = db
