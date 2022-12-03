# Generated by Django 4.1.3 on 2022-12-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScammerHuntCore', '0006_rename_user_name_priorityuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scammer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='scrapedata',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='scrapedata',
            name='mentioned_users',
        ),
        migrations.RemoveField(
            model_name='scrapedata',
            name='reference_link',
        ),
        migrations.RemoveField(
            model_name='scrapedata',
            name='scammer',
        ),
        migrations.RemoveField(
            model_name='scrapedata',
            name='score',
        ),
        migrations.RemoveField(
            model_name='scrapedata',
            name='source',
        ),
        migrations.AlterField(
            model_name='scammer',
            name='phone_number',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]