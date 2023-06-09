# Generated by Django 4.2.2 on 2023-06-20 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_vinhos_acidez_fixa_alter_vinhos_acidez_volátil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinhos',
            name='acidez_fixa',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='acidez_volátil',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='acido_cítrico',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='acucar_residual',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='cloretos',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='densidade',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='dióxido_de_enxofre_livre',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='dióxido_de_enxofre_total',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='pH',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='sulfatos',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='álcool',
            field=models.DecimalField(decimal_places=6, max_digits=10),
        ),
    ]
