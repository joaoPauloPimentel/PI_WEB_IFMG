# Generated by Django 4.1.7 on 2023-10-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PI_WEB', '0002_alter_ferramenta_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferramenta',
            name='imagem',
            field=models.ImageField(default='default.png', upload_to='./media/ferramentas'),
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='tipo',
            field=models.CharField(choices=[('Perigoso', 'Perigoso'), ('Seguro', 'Seguro')], max_length=10),
        ),
    ]
