from peewee import *

db = SqliteDatabase('students.db')


class Student(Model):
    # Always name models with singular name
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)
    # Tell model what database it belongs to
    # Do that with class, inside of the class 
    class Meta:
        database = db

students = [
    {u'username': 'kennethlove',
    'points': 4888}
]

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)