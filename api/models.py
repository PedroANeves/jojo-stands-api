from django.db import models
from django.utils.translation import gettext_lazy as _


class Stand(models.Model):
    stand_name = models.CharField(max_length=30)
    stand_user = models.CharField(max_length=30)


    class Stat(models.TextChoices):
        VERY_GOOD = 'A', _("Very Good")
        GOOD = 'B', _("Good")
        AVERAGE = 'C', _("Average")
        POOR = 'D', _("Poor")
        VERY_POOR = 'E', _("Very Poor")
        NONE = '∅', _("None")
        INFINITE = '∞', _("Infinite")
        UNKNOWN = '?', _("Unknown")
    

    destructive_power_stat = models.CharField(
        max_length = 1,
        choices = Stat.choices,
        default = Stat.UNKNOWN,
    )
    speed_stat = models.CharField(
        max_length = 1,
        choices = Stat.choices,
        default = Stat.UNKNOWN,
    )
    range_stat = models.CharField(
        max_length = 1,
        choices = Stat.choices,
        default = Stat.UNKNOWN,
    )
    stamina_stat = models.CharField(
        max_length = 1,
        choices = Stat.choices,
        default = Stat.UNKNOWN,
    )
    precision_stat = models.CharField(
        max_length = 1,
        choices = Stat.choices,
        default = Stat.UNKNOWN,
    )
    development_potential_stat = models.CharField(
        max_length = 1,
        choices = Stat.choices,
        default = Stat.UNKNOWN,
    )

    def __str__(self):
        return f'{self.stand_name}({self.stand_user})\
            [{self.destructive_power_stat},\
            {self.speed_stat},\
            {self.range_stat},\
            {self.stamina_stat},\
            {self.precision_stat},\
            {self.development_potential_stat}]'
    
