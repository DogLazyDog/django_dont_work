from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    grade = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    