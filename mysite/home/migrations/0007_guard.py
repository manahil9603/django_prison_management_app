# Generated by Django 3.2.18 on 2023-04-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_sho'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('shift', models.CharField(max_length=50)),
            ],
        ),
    ]
