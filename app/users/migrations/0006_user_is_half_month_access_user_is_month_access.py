# Generated by Django 4.0.1 on 2022-12-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_barangay_user_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_half_month_access',
            field=models.BooleanField(default=True, verbose_name='is_half_month_access'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_month_access',
            field=models.BooleanField(default=True, verbose_name='is_month_access'),
        ),
    ]
