# Generated by Django 4.1.3 on 2022-12-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScammerHuntCore', '0013_scrapedata_scammerhunt_referen_9bdad7_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapedata',
            name='sentiment_score',
            field=models.FloatField(default=0.0),
        ),
    ]
