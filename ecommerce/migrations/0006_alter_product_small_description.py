# Generated by Django 5.0.1 on 2024-01-26 11:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='small_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='small description', null=True),
        ),
    ]