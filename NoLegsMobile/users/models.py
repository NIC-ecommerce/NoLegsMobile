from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    DRIVER = 'driver'
    PASSENGER = 'passenger'
    ROLE_CHOICES = [
        (DRIVER, 'Driver'),
        (PASSENGER, 'Passenger'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    car_model=models.CharField(max_length=255)
    phone = models.IntegerField(default=87751234567)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_groups'  # Новое имя обратной связи
    )

    # Пример для поля user_permissions
    # Добавляем или изменяем related_name
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_permissions'  # Новое имя обратной связи
    )

