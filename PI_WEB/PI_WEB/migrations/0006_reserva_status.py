# Generated by Django 4.2.6 on 2023-10-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PI_WEB', '0005_groups_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='status',
            field=models.CharField(default='Pendente', max_length=20),
        ),
    ]
