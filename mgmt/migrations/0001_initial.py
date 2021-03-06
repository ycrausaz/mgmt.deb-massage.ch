# Generated by Django 3.2.9 on 2022-01-26 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_first_name', models.CharField(max_length=80, verbose_name='Prénom')),
                ('client_last_name', models.CharField(max_length=80, verbose_name='Nom')),
                ('client_birthdate', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('client_address', models.CharField(blank=True, max_length=80, null=True, verbose_name='Adressse')),
                ('client_additional_address', models.CharField(blank=True, max_length=80, null=True, verbose_name="Complément d'adresse")),
                ('client_zip_code', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='NPA')),
                ('client_city', models.CharField(blank=True, max_length=80, null=True, verbose_name='Localité')),
                ('client_phone_number_1', models.CharField(blank=True, help_text='Format : +xx xx xxx xx xx (Exemple : +41 79 123 45 67)', max_length=30, verbose_name='Téléphone 1')),
                ('client_phone_number_2', models.CharField(blank=True, help_text='Format : +xx xx xxx xx xx (Exemple : +41 79 123 45 67)', max_length=30, verbose_name='Téléphone 2')),
                ('client_email_address', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('client_comment', models.TextField(blank=True, null=True, verbose_name='Commentaire')),
            ],
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('massage_id', models.AutoField(primary_key=True, serialize=False)),
                ('massage_name', models.CharField(max_length=80, verbose_name='Nom du massage')),
                ('massage_duration', models.PositiveSmallIntegerField(verbose_name='Durée (minutes)')),
                ('massage_price', models.FloatField(verbose_name='Prix par heure')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_date', models.DateTimeField(verbose_name='Date du massage')),
                ('service_duration', models.PositiveSmallIntegerField(verbose_name='Durée du massage (en minutes)')),
                ('service_comment', models.TextField(blank=True, verbose_name='Remarque')),
                ('service_cashed_price', models.FloatField(verbose_name='Montant encaissé')),
                ('service_client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mgmt.client', verbose_name='Client')),
                ('service_massage_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mgmt.massage', verbose_name='Massage')),
            ],
        ),
    ]
