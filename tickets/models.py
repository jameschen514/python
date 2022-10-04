from django.db import models
from datetime import datetime
# Create your models here.

class Ticket(models.Model):
    #id = models.IntegerField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    DEFECT = 'D'
    FEATURE = 'F'
    PATCH = 'P'

    TICKET_TYPE = (
        (DEFECT, 'Defect'),
        (FEATURE, 'Feature'),
        (PATCH, 'Patch'),
    )

    ticket_type = models.CharField(max_length=1, choices=TICKET_TYPE, default=DEFECT)

    NEW = 'N'
    READ = 'R'
    WAITING = 'W'
    REOPENED = 'RP'
    RESOLVED = 'RS'

    TICKET_STATUS = (
        (NEW, 'New'),
        (READ, 'Read'),
        (WAITING, 'Waiting'),
        (REOPENED, 'Reopened'),
        (RESOLVED, 'Resolved'),
    )

    ticket_status = models.CharField(max_length=1, choices=TICKET_STATUS, default=NEW)

    time = datetime.now()
    #now = time.strftime("%Y-%m-%d %H:%M:%S.%f")
    now = datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S.%f")
    ############################################
    updated = models.CharField(max_length=19, default=now)

    owner = models.CharField(max_length=18, default='noname')

    # attachment = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.subject

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20, default='bug')
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=18)

    ACTIVE = 'A'
    DISABLED = 'D'
    PENDING = 'P'

    USER_STATUS = (
        (ACTIVE, 'Active'),
        (DISABLED, 'Disabled'),
        (PENDING, 'Pending'),
    )

    user_status = models.CharField(max_length=1, choices=USER_STATUS, default=DISABLED)

    created = models.DateField(auto_now=False, auto_now_add=False)
    last_login = models.DateField(auto_now=False, auto_now_add=True)

    OPERATOR = 'O'
    POWER = 'P'
    READ = 'R'
    ADMINISTRATOR = 'A'

    USER_TYPE = (
        (OPERATOR, 'Operator'),
        (POWER, 'Power'),
        (READ, 'Read'),
        (ADMINISTRATOR, 'Administrator'),
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPE, default=OPERATOR)

    def __str__(self):
        return self.username
