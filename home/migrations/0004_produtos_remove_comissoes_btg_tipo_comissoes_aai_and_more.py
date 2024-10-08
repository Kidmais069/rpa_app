# Generated by Django 4.2.9 on 2024-04-04 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_rename_info_comissoes_btg_nome_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Produtos",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(default="", max_length=100)),
                ("tipo", models.CharField(default="", max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name="comissoes_btg",
            name="tipo",
        ),
        migrations.CreateModel(
            name="Comissoes_AAI",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("corretagem_percentual", models.FloatField(blank=True, null=True)),
                (
                    "nome",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.produtos"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="comissoes_btg",
            name="nome",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.produtos"
            ),
        ),
    ]
