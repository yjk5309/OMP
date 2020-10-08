# Generated by Django 3.0.5 on 2020-10-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_accounts', '0005_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_seller',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(blank=True, default=2),
        ),
        migrations.DeleteModel(
            name='Seller',
        ),
    ]
