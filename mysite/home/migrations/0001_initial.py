# Generated by Django 3.2.18 on 2023-04-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('pid', models.IntegerField(verbose_name='')),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]