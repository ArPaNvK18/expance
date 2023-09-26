# Generated by Django 3.2.6 on 2023-09-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countApp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddAll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_Type', models.CharField(max_length=200)),
                ('Transaction_Type', models.CharField(max_length=200)),
                ('Rs', models.IntegerField(max_length=200)),
                ('Comment', models.CharField(max_length=400)),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AddData',
        ),
    ]
