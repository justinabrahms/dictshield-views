# Standard library
import datetime

# Imports from dictshield proper
from dictshield.document import Document
from dictshield.fields import StringField, DateTimeField

# Imports from our package
from dictshield.views import WhitelistView


class Post(Document):
    name = StringField()
    body = StringField()
    username = StringField()
    password = StringField()
    created_time = DateTimeField()


class Public(WhitelistView):
    fields = ['name', 'body']


entry = Post(name='Some clever post name',
             body='blah blah blah',
             username='marca',
             password='password',
             created_time=datetime.datetime.now())
print("entry.name = %r" % entry.name)
print("entry.created_time = %r" % entry.created_time)
print("entry.password = %r" % entry.password)
print("")

entry_view = Public(entry)

print("entry_view.name = %r" % entry_view.name)
print("entry_view.password = %r" % entry_view.password)
