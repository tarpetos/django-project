from django.db import models

class User(models.Model):
    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='First name'
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Last name'
    )

    patronymic = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Patronymic',
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name='Date of birth',
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name='Photo',
        null=True
    )

    telegram_id = models.CharField(
        max_length=20,
        blank=False,
        verbose_name='Telegram ID'
    )

    user_country = models.ForeignKey(
        'Country',
        verbose_name='Country',
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )

    notes = models.TextField(
        blank=True,
        verbose_name='Additional notes'
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)

        return full_name.strip()
