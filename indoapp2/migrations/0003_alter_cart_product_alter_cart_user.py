# Generated by Django 4.2.3 on 2023-09-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indoapp2', '0002_alter_deliverydetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.IntegerField(),
        ),
    ]
