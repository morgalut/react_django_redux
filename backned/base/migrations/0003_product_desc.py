# Generated by Django 5.0.3 on 2024-03-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_product_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
