# Generated by Django 3.0.5 on 2020-05-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200502_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='description',
            field=models.TextField(max_length=500000),
        ),
    ]
