# Generated by Django 5.1.3 on 2024-12-16 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_mentor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='code',
            new_name='mentorCd',
        ),
    ]
