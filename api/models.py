from django.db import models

# Create your models here.
class Items(models.Model):
   item_name  = models.CharField(max_length=20, default="Item")
   id  = models.AutoField(primary_key=True)
   price = models.FloatField(default=0.0)
   image = models.URLField(max_length=200, default="https://ik.imagekit.io/demo/tr:di-medium_cafe_B1iTdD0C.jpg/non_existent_image.jpg")