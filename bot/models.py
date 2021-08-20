from peewee import SqliteDatabase, Model, IntegerField, BooleanField, CharField

from settings import DATABASE_PATH


database = SqliteDatabase(DATABASE_PATH)


# base model for other models
class BaseModel(Model):
    class Meta:
        database = database


# model that represents user
class User(BaseModel):
    user_id = IntegerField(primary_key=True, unique=True)
    active = BooleanField(default=True)
    requests = IntegerField(default=0)


# model that represents source
class Source(BaseModel):
    name = CharField(max_length=40)
    users = IntegerField(default=0)
