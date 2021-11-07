# Generated by Django 3.2.7 on 2021-11-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stand',
            name='stand_part',
            field=models.IntegerField(choices=[(None, 'Part unknown'), (0, 'No part'), (1, 'Real Life Stand'), (2, 'Purple Haze Feedback Light Novel'), (3, 'Part 3, Stardust Crusaders.'), (4, 'Part 4, Diamond Is Unbreakable.'), (5, 'Part 5, Golden Wind.'), (6, 'Part 6, Stone Ocean.'), (7, 'Part 7, Steel Ball Run.'), (8, 'Part 8, JoJolion.')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='stand',
            name='destructive_power_stat',
            field=models.CharField(choices=[('A', '(A) Very Good'), ('B', '(B) Good'), ('C', '(C) Average'), ('D', '(D) Poor'), ('E', '(E) Very Poor'), ('∅', '(∅) None'), ('∞', '(∞) Infinite'), ('?', '(?) Unknown')], default='?', max_length=1),
        ),
        migrations.AlterField(
            model_name='stand',
            name='development_potential_stat',
            field=models.CharField(choices=[('A', '(A) Very Good'), ('B', '(B) Good'), ('C', '(C) Average'), ('D', '(D) Poor'), ('E', '(E) Very Poor'), ('∅', '(∅) None'), ('∞', '(∞) Infinite'), ('?', '(?) Unknown')], default='?', max_length=1),
        ),
        migrations.AlterField(
            model_name='stand',
            name='precision_stat',
            field=models.CharField(choices=[('A', '(A) Very Good'), ('B', '(B) Good'), ('C', '(C) Average'), ('D', '(D) Poor'), ('E', '(E) Very Poor'), ('∅', '(∅) None'), ('∞', '(∞) Infinite'), ('?', '(?) Unknown')], default='?', max_length=1),
        ),
        migrations.AlterField(
            model_name='stand',
            name='range_stat',
            field=models.CharField(choices=[('A', '(A) Very Good'), ('B', '(B) Good'), ('C', '(C) Average'), ('D', '(D) Poor'), ('E', '(E) Very Poor'), ('∅', '(∅) None'), ('∞', '(∞) Infinite'), ('?', '(?) Unknown')], default='?', max_length=1),
        ),
        migrations.AlterField(
            model_name='stand',
            name='speed_stat',
            field=models.CharField(choices=[('A', '(A) Very Good'), ('B', '(B) Good'), ('C', '(C) Average'), ('D', '(D) Poor'), ('E', '(E) Very Poor'), ('∅', '(∅) None'), ('∞', '(∞) Infinite'), ('?', '(?) Unknown')], default='?', max_length=1),
        ),
        migrations.AlterField(
            model_name='stand',
            name='stamina_stat',
            field=models.CharField(choices=[('A', '(A) Very Good'), ('B', '(B) Good'), ('C', '(C) Average'), ('D', '(D) Poor'), ('E', '(E) Very Poor'), ('∅', '(∅) None'), ('∞', '(∞) Infinite'), ('?', '(?) Unknown')], default='?', max_length=1),
        ),
        migrations.AlterField(
            model_name='stand',
            name='stand_user',
            field=models.CharField(max_length=50),
        ),
    ]