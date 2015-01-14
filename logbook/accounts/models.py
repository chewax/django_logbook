from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from user_settings.models import UserSettings


class SimpleModelMixin(models.Model):
    name = models.CharField(max_length=50)
    shorthand = models.CharField(max_length=4)

    TYPE = [("RAT", "Rating"), ("TRAT", "Type Rating"), ("LIC", "License")]
    type = models.CharField(max_length=30, null=False, blank=True, choices=TYPE)

    description = models.TextField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name


class License(SimpleModelMixin):
    pass


class Rating(SimpleModelMixin):
    pass


class UserManager(BaseUserManager):

    def create_user(self, username, email=None,
                    password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)

        user = self.model(username=username, email=email)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, email=None):
        email = UserManager.normalize_email(email)
        user = self.create_user(username, email, password)
        user.is_superuser = True

        user.save(using=self._db)

        return user


# USERS
class User(AbstractUser):

    enabled = models.BooleanField(default=True)

    display_real_name = models.BooleanField(default=False)
    preferred_timezone = models.CharField(max_length=32, default='Automatic')
    license_number = models.CharField(max_length=15, blank=True)

    licences = models.ManyToManyField(License, blank=True, null=True)
    ratings = models.ManyToManyField(Rating, blank=True, null=True)

    settings = models.OneToOneField(UserSettings, null=True,
                                    related_name='user_settings')

    objects = UserManager()

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def get_full_name(self):
        if self.display_real_name:
            return super(User).get_full_name()
        else:
            return self.username

    def clean(self):
        # Assign settings to user
        self.settings = UserSettings.objects.get_or_create(name=self.username)[0]
        self.save()
        return super(User, self).clean()
