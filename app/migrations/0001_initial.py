# Generated by Django 3.2.13 on 2022-05-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=70, null=True)),
                ('day', models.CharField(max_length=70, null=True)),
                ('reminder', models.BooleanField()),
            ],
        ),
    ]
