from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):

    username = models.CharField('username', max_length=150, unique=True, default="")
    full_name = models.TextField()
    password= models.TextField()
    email = models.EmailField(unique=True, blank=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return str(self.username)



class Todo(models.Model):
    task = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    CATAEGORY_CHOICES = (
        ('urgent', 'URGENT'),
        ('important', 'IMPORTANT'),
        ('unimportant', 'UNIMPORTANT'),
    )

    cataegory = models.CharField(max_length=15, choices=CATAEGORY_CHOICES, default='important')
    task_completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=now, editable=False)
    due_on = models.DateField(default=now)
    time = models.TimeField(default=now)

    class Meta:
        db_table = "todo"
    def __str__(self):
        return str(self.name)


