from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    ENGINEER = 'Engineer'
    MANAGER = 'Manager'
    ATTENDANT = 'Lab Attendant'
    CLERK = 'Clerk'
    ROLE_CHOICES = [
        (ENGINEER, 'Engineer'),
        (MANAGER, 'Manager'),
        (ATTENDANT, 'Lab Attendant'),
        (CLERK, 'Clerk'),
    ]

    type = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self) -> str:
        return self.type
    
class Key(models.Model):
    keyname = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    total_quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.keyname

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} is a {self.role.type}"
    
class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    accessDateTime = models.DateTimeField(auto_now_add=True)
    returnDateTime = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        if self.returnDateTime:
            return f"{self.user.username} obtained {self.key.keyname} key on {self.accessDateTime.strftime('%d/%m/%Y %I:%M:%S %p')} and returned it on {self.returnDateTime.strftime('%d/%m/%Y %I:%M:%S %p')}"
        return f"{self.user.username} obtained {self.key.keyname} key on {self.accessDateTime.strftime('%d/%m/%Y %I:%M:%S %p')}"
    
class Permission(models.Model):
    READ = 'Read'
    Write = 'Write'
    levels = [
        (READ, 'Read'),
        (Write, 'Write'),
    ]
    level = models.CharField(max_length=10, default='Read' ,choices=levels)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    key = models.ForeignKey(Key, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.role.type} has {self.level} permission for {self.key.keyname}"