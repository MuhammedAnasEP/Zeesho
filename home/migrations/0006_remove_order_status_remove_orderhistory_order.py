# Generated by Django 4.1.2 on 2022-11-14 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_order_status_orderhistory_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='orderhistory',
            name='order',
        ),
    ]
