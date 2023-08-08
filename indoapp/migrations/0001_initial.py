# Generated by Django 4.2.3 on 2023-07-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndoUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'IndoUsers',
            },
        ),
    ]
