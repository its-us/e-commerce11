# Generated by Django 5.0.1 on 2024-01-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_alter_cartorder_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='order_date',
            field=models.DateTimeField(),
        ),
    ]