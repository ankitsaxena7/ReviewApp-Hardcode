from django.db import models

# Create your models here.
# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    createdate = models.DateTimeField()

    def __str__(self):
        return self.first_name



class Review(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    rating = models.IntegerField()
    reviewto = models.CharField(max_length=30)
    reviewdesc = models.CharField(max_length=30)
    reviewdate = models.DateTimeField()

    def __str__(self):
        return str(self.users)