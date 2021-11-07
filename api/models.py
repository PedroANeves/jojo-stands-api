from django.db import models
from django.utils.translation import gettext_lazy as _


class Stand(models.Model):
    stand_name = models.CharField(max_length=30)
    stand_user = models.CharField(max_length=50)
    

    class Part(models.IntegerChoices):
        PART_UNKNOWN = 0, _('No part')
        REAL_LIFE = 1, _('Real Life Stand')
        PURPLE_HAZE_LN = 2, _('Purple Haze Feedback Light Novel')
        PART_THREE = 3, _('Part 3, Stardust Crusaders.')
        PART_FOUR = 4, _('Part 4, Diamond Is Unbreakable.')
        PART_FIVE = 5, _('Part 5, Golden Wind.')
        PART_SIX = 6, _('Part 6, Stone Ocean.')
        PART_SEVEN = 7, _('Part 7, Steel Ball Run.')
        PART_EIGHT = 8, _('Part 8, JoJolion.')
        __empty__ = _('Part unknown')
    

    stand_part = models.IntegerField(
        choices = Part.choices,
        default = Part.PART_UNKNOWN
    )


    class Stat(models.TextChoices):
        VERY_GOOD = 'A', _("(A) Very Good")
        GOOD = 'B', _("(B) Good")
        AVERAGE = 'C', _("(C) Average")
        POOR = 'D', _("(D) Poor")
        VERY_POOR = 'E', _("(E) Very Poor")
        NONE = '∅', _("(∅) None")
        INFINITE = '∞', _("(∞) Infinite")
        UNKNOWN = '?', _("(?) Unknown")
    

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
    
