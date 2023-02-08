from django.db import models

class Country(models.Model):
    country_name = models.CharField(
        max_length=256,
        verbose_name='Country name',
    )

    most_active = models.OneToOneField(
        'User',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Most active user',
    )

    # users_country_number = models.IntegerField(
    #     blank=False,
    #     default = 1,
    #     verbose_name = 'Country users'
    # )


    notes = models.TextField(
        blank=True,
        verbose_name='Additional notes'
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        if self.most_active:
            return  '%s (%s %s)' % (
                self.country_name,
                self.most_active.first_name,
                self.most_active.last_name,
            )
        else:
            return '%s' % (self.country_name)
