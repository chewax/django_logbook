from django.db import models
# from accounts.models import User


class UserSettings(models.Model):

    LANGUAGE_CHOICES = (
        ('EN', 'English'),
        ('ES', 'Spanish'),
    )

    name = models.CharField(max_length=40, null=True)

    language = models.CharField(max_length=2,
                                choices=LANGUAGE_CHOICES,
                                default='EN')

    max_on_1m = models.IntegerField(default=90,
                                    verbose_name="Maximum flight"
                                                 " hours in a month")
    max_on_30 = models.IntegerField(default=90,
                                    verbose_name="Maximum flight"
                                                 " hours in a 30 consecutive"
                                                 " days")

    max_on_90 = models.IntegerField(default=250,
                                    verbose_name="Maximum flight"
                                                 " hours in 90 days")

    max_on_6m = models.IntegerField(default=450,
                                    verbose_name="Maximum flight"
                                                 " hours in 6 months")

    max_on_12m = models.IntegerField(default=900,
                                     verbose_name="Maximum flight "
                                                  "hours in 12 months")

    max_on_1y = models.IntegerField(default=1000,
                                    verbose_name="Maximum flight "
                                                 "hours per year")

    max_service_1m = models.IntegerField(default=150,
                                         verbose_name="Maximum service hours "
                                                      "per month")

    max_service_3m = models.IntegerField(default=400,
                                         verbose_name="Maximum service hours "
                                                      "per 3 month")

    max_service_1y = models.IntegerField(default=150,
                                         verbose_name="Maximum service hours "
                                                      "per year")

    def __init__(self,  *args, **kwargs):
        try:
            self.name = kwargs['name']
        except KeyError:
            self.name = ''

        return super(UserSettings, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.name
