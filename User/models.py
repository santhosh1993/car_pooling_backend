from django.db import models


class User(models.Model):
    USER_TYPE = (
        ('a', 'Admin'),
        ('e', 'Employee'),
        ('d', 'Driver'),
    )

    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100,
                                unique=True)
    user_type = models.CharField(max_length=1,
                                 choices=USER_TYPE,
                                 blank=False,
                                 default='e',
                                 help_text='Select type of User')
    employeeId = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.employeeId} {self.user_name} {self.user_type}"

    @staticmethod
    def authenticate_user(email_id, password):
        user = User.objects.filter(email_id=email_id)
        if user.exists():
            user = user.get()
            if user.password == password:
                return user
        return None

