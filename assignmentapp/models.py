from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	id = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
	Client_Name = models.CharField(max_length=200, null=True)
	Created_at = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name