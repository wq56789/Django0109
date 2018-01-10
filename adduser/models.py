from django.db import models

# Create your models here.
class stuTest(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    jg = models.CharField(max_length=20)
    class Meta:
        db_table='stu'