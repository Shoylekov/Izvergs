# Generated by Django 5.0.3 on 2024-03-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_image_remove_room_upload_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
