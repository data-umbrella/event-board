# Generated by Django 4.0.3 on 2022-08-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='subscribe_to_newsletter',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
