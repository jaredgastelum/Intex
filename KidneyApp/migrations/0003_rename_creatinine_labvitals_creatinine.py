# Generated by Django 4.1.2 on 2022-11-30 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KidneyApp', '0002_labvitals_creatinine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labvitals',
            old_name='creatinine',
            new_name='Creatinine',
        ),
    ]