from django.db import models

class User(models.Model):
  name     = models.CharField(max_length=50)
  email    = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
 
class Data_source(models.Model):
  name = models.CharField(max_length=50)
  
class Mange_store(models.Model):
  store_date        = models.DateTimeField( auto_now_add=True)
  data_source_name  = models.CharField(max_length=50)
  file_name         = models.CharField(max_length=50)
  execution_time    = models.CharField(max_length=50)
  number_of_records = models.IntegerField()
  data_source       = models.ForeignKey(Data_source, on_delete=models.CASCADE)

class Data(models.Model):
  customer_name = models.CharField(max_length=50)
  gender        = models.CharField(max_length=50)
  country       = models.CharField(max_length=50)
  city          = models.CharField(max_length=50)
  state         = models.CharField(max_length=50)
  category      = models.CharField(max_length=50)
  sub_category  = models.CharField(max_length=50)
  product_name  = models.CharField(max_length=50)
  sales         = models.FloatField()
  quantity      = models.IntegerField()
  discount      = models.FloatField()
  profit        = models.FloatField()
  mange_store   = models.ForeignKey(Mange_store, on_delete=models.CASCADE)