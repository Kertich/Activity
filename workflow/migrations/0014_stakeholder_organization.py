# Generated by Django 2.2 on 2019-08-04 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0013_contact_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Organization'),
        ),
    ]
