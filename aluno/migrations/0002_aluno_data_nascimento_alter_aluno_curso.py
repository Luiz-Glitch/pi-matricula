# Generated by Django 5.1 on 2024-09-07 18:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aluno", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aluno",
            name="data_nascimento",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="aluno",
            name="curso",
            field=models.CharField(
                choices=[
                    ("INFORMATICA", "Informática"),
                    ("ALIMENTOS", "Alimentos"),
                    ("APICULTURA", "Apicutura   "),
                ],
                max_length=255,
            ),
        ),
    ]
