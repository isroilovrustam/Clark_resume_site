# Generated by Django 4.1.4 on 2022-12-12 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactme_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
