from django.db import models

class Student(models.Model):
    AVAILABLE_GRADES = (('6A', '6A'),('6B', '6B'),('6C', '6C'),('6D', '6D'),('7A', '7A'),('7B', '7B'),('7C', '7C'),('7D', '7D'),('8A', '8A'),('8B', '8B'),('8C', '8C'),('8D', '8D'),('9A', '9A'),('9B', '9B'),('9C', '9C'),('9D', '9D'),('10A', '10A'),('10B', '10B'),('10C', '10C'),('11A', '11A'),('11B', '11B'),('11C', '11C'),);
    name = models.CharField(blank=True, max_length=100)
    code = models.IntegerField(blank=True, null=True)
    mail = models.EmailField(blank=True, max_length=100)
    age = models.IntegerField(blank = True)
    grade = models.CharField(choices= AVAILABLE_GRADES, max_length=10)

    def __str__(self):
        return self.name;
