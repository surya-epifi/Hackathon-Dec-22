# Generated by Django 4.1.3 on 2022-12-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScammerHuntCore', '0016_upi_scammer_scaupi_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scammer',
            name='scaupi_ids',
        ),
        migrations.RemoveField(
            model_name='scammer',
            name='upi_id',
        ),
        migrations.AddField(
            model_name='scammer',
            name='upi_ids',
            field=models.ManyToManyField(default=None, null=True, to='ScammerHuntCore.upi'),
        ),
    ]
