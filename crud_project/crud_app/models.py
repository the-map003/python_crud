from django.db import models


class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	registration_number = models.CharField(max_length=30, unique=True)
	course = models.CharField(max_length=120)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return f"{self.first_name} {self.last_name} ({self.registration_number})"
