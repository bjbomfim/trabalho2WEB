# Generated by Django 4.1.3 on 2022-11-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
