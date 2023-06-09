# Generated by Django 4.2 on 2023-04-30 15:36
# Dados dos produtos que foram adicionados ao sistema
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade no estoque: ')),
            ],
        ),
    ]
