from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

def user_avatar_directory_path(instance: "User", filename: str) -> str:
    return "users/user_{pk}/{username}/{filename}".format(
        pk=instance.user.pk,
        username=instance.user.username,
        filename=filename,
    )


class Profile(models.Model):
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_avatar_directory_path, default='default.png')
