# Generated by Django 4.1.3 on 2022-12-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScammerHuntCore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PriorityUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='source',
            field=models.CharField(choices=[('TWITTER', 'TWITTER')], default='TWITTER', max_length=50),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='keywords',
            field=models.ManyToManyField(to='ScammerHuntCore.keywords'),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='mentioned_users',
            field=models.ManyToManyField(to='ScammerHuntCore.priorityuser'),
        ),
    ]
