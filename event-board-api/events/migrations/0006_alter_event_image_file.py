# Generated by Django 4.0.3 on 2022-07-25 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image_file',
            field=models.FileField(blank=True, null=True, upload_to='event_image_files'),
        ),
    ]
