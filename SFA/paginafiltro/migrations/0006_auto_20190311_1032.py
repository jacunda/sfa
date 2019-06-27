# Generated by Django 2.1.7 on 2019-03-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginafiltro', '0005_auto_20190310_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='EBIT12',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='EBIT3',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='EBIT_ATIVO',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='LPA',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Lucro_liq12',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='PAtivCircLiq',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='PAtivos',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='PCap_Giro',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='PEBIT',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='PL',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='PSR',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='PVP',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ROE',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ROIC',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='VPA',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ativo',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ativo_circulante',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cotacao',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='crescimento_receita5',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='data',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='diBrPat',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='disponibilidades',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='div_bruta',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='div_liquida',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='dividend_yield',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='empresa',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ev_ebit',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='giro_ativos',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='liquidez_corr',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='lucro_liq3',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='marg_EBIT',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='marg_bruta',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='marg_liquida',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='max52',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='min52',
            field=models.DecimalField(blank=True, decimal_places=20, default=0.0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='num_acoes',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='papel',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='patrim_liq',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='receita_liq12',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='receita_liq3',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='setor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='subsetor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ultimo_balanco',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='valor_de_mercado',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='valor_firma',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='volume',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
