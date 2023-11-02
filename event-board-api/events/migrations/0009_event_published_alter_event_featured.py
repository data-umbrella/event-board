# Generated by Django 4.0.3 on 2022-07-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_event_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
