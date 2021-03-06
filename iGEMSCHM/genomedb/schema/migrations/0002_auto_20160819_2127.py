# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('species_key', models.CharField(max_length=200)),
                ('accession_key', models.CharField(max_length=200)),
                ('strand', models.IntegerField()),
                ('start', models.IntegerField()),
                ('stop', models.IntegerField()),
                ('genebank_annotation', models.CharField(max_length=200)),
                ('cluster_information', models.CharField(max_length=200)),
                ('operon_key', models.CharField(max_length=200)),
                ('gene_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HMM_Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('accession_key', models.CharField(max_length=200)),
                ('species_key', models.CharField(max_length=200)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('hmm_profile_key', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HMM_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Operon_Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('kegg_orthology_ID', models.CharField(max_length=200)),
                ('species_key', models.CharField(max_length=200)),
                ('operon_name', models.CharField(max_length=200)),
                ('annotation', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='accession',
            old_name='key_assembly',
            new_name='assembly_key',
        ),
        migrations.AlterField(
            model_name='accession',
            name='species_key',
            field=models.CharField(max_length=200),
        ),
    ]
