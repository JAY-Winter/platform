# Generated by Django 3.2.13 on 2022-12-11 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221211_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interest',
            field=models.ManyToManyField(blank=True, to='accounts.Interest'),
        ),
    ]
