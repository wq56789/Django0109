# Generated by Django 2.0 on 2018-01-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stuTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('jg', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'stu',
            },
        ),
    ]