from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, null=True)
    address = models.TextField()
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='foods')
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="food")
    price = models.PositiveIntegerField(null=True)
    discount = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return self.title