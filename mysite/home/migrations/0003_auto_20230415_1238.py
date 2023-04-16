# Generated by Django 3.2.18 on 2023-04-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contact_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prisoner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('EnteranceDate', models.DateTimeField(verbose_name='')),
                ('ReleaseDate', models.DateTimeField(verbose_name='')),
                ('SecurityLevel', models.CharField(max_length=50)),
                ('cellSharing', models.CharField(max_length=50)),
                ('CurrentDate', models.DateTimeField(verbose_name='')),
            ],
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='pid',
            new_name='Pid',
        ),
    ]
