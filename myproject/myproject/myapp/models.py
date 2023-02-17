
from django.db import models

# Create your models here.


class Myapp (models.Model):
 id = models.IntegerField(primary_key=True)
staffname = models.AutoField(max_length=40, blank=True)
role= models.AutoField(max_length=50, blank=True)
hireddate= models.IntegerField(max_length=10, blank=True)



class Meta:
    db_table = 'myproject'