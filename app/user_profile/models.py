from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    pass
    # current_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    #
    # follower = models.ManyToManyField(to=User)

    # friend = models.ManyToManyField(to=User)

    def __str__(self):
        return f'User Profile: {self.current_user} is followed by: {self.follower}'
