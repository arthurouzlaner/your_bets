from django.db import models


class PersonalData(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    email = models.EmailField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return ", ".join([self.name, self.nickname, self.email])
