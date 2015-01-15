from django.db import models

class CrewMember(models.Model):

    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    ROLE_CHOICES = (
        ('PIC', 'Pilot in command'),
        ('SIC', 'Second in command'),
        ('INT', 'Instructor'),
        ('INP', 'Inspector'),
        ('ENG', 'Engineer'),
        ('NAV', 'Navigator'),
        ('CCR', 'Cabin Crew'),
    )
    # PIC/SIC/ENG/NAV/CCREW
    role = models.CharField(max_length=4, blank=True,
                            default="PIC", choices=ROLE_CHOICES)

    phone_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{} {} - {}'.format(self.first_name, self.last_name, self.role)

