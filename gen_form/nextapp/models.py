from django.db import models

# Create your models here.
class re_me(models.Model):
    b_name=models.CharField(max_length=20)
    l_band=models.CharField(max_length=30)
    contact=models.CharField(max_length=40)
    num_mem=models.CharField(max_length=40)
    num_band_mem=models.CharField(max_length=40)
    establi_date=models.DateField(max_length=20)
    link_social=models.CharField(max_length=30)
    group_ph=models.FileField(upload_to='images/')
    des=models.CharField(max_length=60)
    ca=models.CharField(max_length=10)
    class Meta:
        db_table="reg"