# Generated by Django 3.2.6 on 2023-09-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Type', models.CharField(max_length=200)),
                ('Transaction_Type', models.CharField(max_length=200)),
                ('Comment', models.CharField(max_length=400)),
            ],
        ),
    ]
