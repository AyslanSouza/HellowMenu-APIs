# Generated by Django 5.0.3 on 2024-05-24 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='nome do usuario', max_length=100)),
                ('senha', models.CharField(help_text='senha do usuario', max_length=100)),
                ('email', models.EmailField(help_text='email do usuario', max_length=100)),
                ('cpf', models.CharField(help_text='cpf do usuario', max_length=14)),
                ('restaurante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardapio.restaurante')),
            ],
        ),
    ]
