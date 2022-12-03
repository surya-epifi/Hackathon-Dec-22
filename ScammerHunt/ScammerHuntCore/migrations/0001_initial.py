# Generated by Django 4.1.3 on 2022-12-03 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scammer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300)),
                ('phone_number', models.CharField(max_length=300)),
                ('email', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_data', models.TextField()),
                ('score', models.IntegerField()),
                ('reference_link', models.TextField()),
                ('scammer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ScammerHuntCore.scammer')),
            ],
        ),
    ]
