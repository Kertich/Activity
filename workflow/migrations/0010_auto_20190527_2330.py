# Generated by Django 2.2.1 on 2019-05-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0009_auto_20190527_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityuser',
            name='organizations',
            field=models.ManyToManyField(blank=True, related_name='organization', to='workflow.Organization', verbose_name='Accessible Organizations'),
        ),
        migrations.AlterField(
            model_name='program',
            name='country',
            field=models.ManyToManyField(blank=True, to='workflow.Country'),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Program Name'),
        ),
    ]
