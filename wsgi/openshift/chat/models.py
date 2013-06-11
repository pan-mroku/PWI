from datetime import datetime
from time import timezone
import uuid
from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    create_date = models.DateTimeField(datetime.now())
    def __unicode__(self):
        return self.nickname
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Message(models.Model):
    id = str(uuid.uuid4())
    user = models.ForeignKey(User)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(datetime.now())
    def __unicode__(self):
        return self.value
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



#http://djangosnippets.org/snippets/1262/
class UUIDField(models.CharField) :

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64 )
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        if add :
            value = str(uuid.uuid4())
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)


