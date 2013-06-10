from datetime import datetime
from time import timezone
from django.db import models

class StringTest(models.Model):
    value = models.CharField(max_length=200)
    pub_date = models.DateTimeField(datetime.now())
    def __unicode__(self):
        return self.pub_date.__str__()+" - "+self.value
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



