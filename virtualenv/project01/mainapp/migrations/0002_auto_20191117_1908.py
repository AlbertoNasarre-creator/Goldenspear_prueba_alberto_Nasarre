# Generated by Django 2.0.5 on 2019-11-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanel',
            name='model_pic',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to=''),
        ),
    ]
