# Generated by Django 4.1.3 on 2022-12-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScammerHuntCore', '0012_scammer_carrier_scammer_geocoder_scammer_timezone'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='scrapedata',
            index=models.Index(fields=['reference_link'], name='ScammerHunt_referen_9bdad7_idx'),
        ),
    ]
