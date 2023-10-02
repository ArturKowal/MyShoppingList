from django.db import models


class Room(models.Model):
    code = models.IntegerField("User code to personal room", blank=False, null=False, unique=True, default=1234)
    name = models.CharField("Room's name", max_length=30, blank=True, null=True)
    description = models.CharField("Room's description", max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user_name = models.CharField("User name", max_length=30, blank=False, null=False)
    email = models.EmailField("Address Email")
    room_code = models.ForeignKey(Room, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.email
