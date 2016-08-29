# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 21:08
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_auto_20160822_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accession',
            name='assembly_key',
        ),
        migrations.RemoveField(
            model_name='accession',
            name='species_key',
        ),
        migrations.RemoveField(
            model_name='gene',
            name='accession_key',
        ),
        migrations.RemoveField(
            model_name='gene',
            name='operon_key',
        ),
        migrations.RemoveField(
            model_name='gene',
            name='species_key',
        ),
        migrations.RemoveField(
            model_name='hmm_output',
            name='accession_key',
        ),
        migrations.RemoveField(
            model_name='hmm_output',
            name='species_key',
        ),
        migrations.RemoveField(
            model_name='operon_database',
            name='species_key',
        ),
        migrations.AddField(
            model_name='accession',
            name='key',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='accession',
            name='species_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schema.Species'),
        ),
        migrations.AddField(
            model_name='gene',
            name='EC_num',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='accession_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.Accession'),
        ),
        migrations.AddField(
            model_name='gene',
            name='function',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='gene',
            name='gene_synonym',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), null=True, size=None),
        ),
        migrations.AddField(
            model_name='gene',
            name='gi',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='locus_tag',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='note',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='gene',
            name='operon_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.Operon_Database'),
        ),
        migrations.AddField(
            model_name='gene',
            name='protein_id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='gene',
            name='protein_product',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='gene',
            name='species_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schema.Species'),
        ),
        migrations.AddField(
            model_name='gene',
            name='translation',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='gene',
            name='uniprot',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='hmm_output',
            name='accession_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schema.Accession'),
        ),
        migrations.AddField(
            model_name='operon_database',
            name='species_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schema.Species'),
        ),
        migrations.AddField(
            model_name='species',
            name='strain',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='species',
            name='sub_strain',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='species',
            name='subspecies',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='species',
            name='taxon',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='accession',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='gene',
            name='cluster_information',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='gene',
            name='gene_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='genebank_annotation',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='gene',
            name='key',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='gene',
            name='start',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='stop',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='strand',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hmm_output',
            name='end',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hmm_output',
            name='hmm_profile_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schema.HMM_Profile'),
        ),
        migrations.AlterField(
            model_name='hmm_output',
            name='key',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='hmm_output',
            name='start',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hmm_profile',
            name='key',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='hmm_profile',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='operon_database',
            name='annotation',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='operon_database',
            name='kegg_orthology_ID',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='operon_database',
            name='key',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='operon_database',
            name='operon_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='species',
            name='key',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]