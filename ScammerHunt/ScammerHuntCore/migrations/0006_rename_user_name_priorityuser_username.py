# Generated by Django 4.1.3 on 2022-12-03 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ScammerHuntCore', '0005_alter_scrapedata_scammer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priorityuser',
            old_name='user_name',
            new_name='username',
        ),
    ]
