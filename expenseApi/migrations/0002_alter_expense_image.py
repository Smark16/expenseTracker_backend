# Generated by Django 4.2.6 on 2024-05-05 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]