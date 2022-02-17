# Generated by Django 3.1.1 on 2021-01-08 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255)),
                ('place_of_execution', models.CharField(blank=True, max_length=255)),
                ('awarning_authority', models.CharField(blank=True, max_length=255)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('tender_viewed', models.BooleanField(default=False)),
                ('publication_date', models.CharField(blank=True, max_length=255)),
                ('closing_date', models.CharField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.country')),
            ],
        ),
    ]
