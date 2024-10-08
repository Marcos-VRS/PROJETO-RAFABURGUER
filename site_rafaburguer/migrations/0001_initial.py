# Generated by Django 5.1.1 on 2024-09-17 06:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.CreateModel(
            name="ProdutoCadastroModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_do_produto", models.CharField(max_length=50)),
                (
                    "foto_do_produto",
                    models.ImageField(blank=True, upload_to="pictures/%Y/%m"),
                ),
                ("descrição", models.TextField()),
                (
                    "data_de_criação",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="site_rafaburguer.categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cadastro de produtos",
                "verbose_name_plural": "Cadastro de produtos",
            },
        ),
    ]
