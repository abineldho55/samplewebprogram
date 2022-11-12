# Generated by Django 4.1.2 on 2022-11-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, null=True)),
                ('rollno', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
