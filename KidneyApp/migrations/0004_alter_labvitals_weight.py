# Generated by Django 4.1.2 on 2022-11-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KidneyApp', '0003_rename_creatinine_labvitals_creatinine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labvitals',
            name='Weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]