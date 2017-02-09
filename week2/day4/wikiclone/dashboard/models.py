from __future__ import unicode_literals

from django.db import models

class topic(models.Model):
    topic_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author= models.CharField(max_length=200)
    desc = models.TextField(default= 'no data available')
    picture= models.ImageField(default= 'null')
    def __str__(self):
        return self.topic_name

#initially i thought they should be kept as separate classes, but then i thought they should be kept in a singke class        
'''
class description(models.Model):
    topic_name = models.ForeignKey(topic, on_delete=models.CASCADE)
    topic_id=models.CharField(max_length=100)
    desc = models.TextField()
    picture= models.ImageField()
    def __str__(self):
        return self.desc
'''