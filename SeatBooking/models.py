from django.db import models


class ServiceType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50,
                            unique=True)

    def __str__(self):
        return f"{self.type}"


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    max_bookings = models.IntegerField()

    def __str__(self):
        return f"{self.service_type} | {self.date_time} | {self.max_bookings}"

    def users(self):
        return self.userbooking_set.all()


class UserBooking(models.Model):
    USER_TURNEDUP_STATUS = (
        ('t', 'Turned Up'),
        ('n', 'None')
    )

    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100, default='')
    employeeId = models.CharField(max_length=100, blank=True, default=0)
    turned_up_status = models.CharField(
        max_length=1,
        choices=USER_TURNEDUP_STATUS,
        blank=True,
        default='n',
        help_text='Turned up status',
    )



