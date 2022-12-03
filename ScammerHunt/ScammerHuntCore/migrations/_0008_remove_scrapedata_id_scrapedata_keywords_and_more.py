# Generated by Django 4.1.3 on 2022-12-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScammerHuntCore', '0007_remove_scammer_id_remove_scrapedata_keywords_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapedata',
            name='id',
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='keywords',
            field=models.ManyToManyField(to='ScammerHuntCore.keywords'),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='mentioned_users',
            field=models.ManyToManyField(to='ScammerHuntCore.priorityuser'),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='reference_link',
            field=models.TextField(default='', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='reply_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='retweet_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='scammer',
            field=models.ManyToManyField(to='ScammerHuntCore.scammer'),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scrapedata',
            name='source',
            field=models.CharField(choices=[('TWITTER', 'TWITTER')], default='TWITTER', max_length=50),
        ),
    ]
