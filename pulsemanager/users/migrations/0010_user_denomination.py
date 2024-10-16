# Generated by Django 2.0.4 on 2018-04-19 22:12

from django.db import migrations
import django.utils.timezone
import pulsemanager.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180419_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='denomination',
            field=pulsemanager.users.models.DenominationField(choices=[('AN', 'Anglican'), ('AG', 'Assemblies of God'), ('BT', 'Baptist'), ('CC', 'Charismatic'), ('CMA', 'Christian Missionary Alliance'), ('COG', 'Church of God'), ('CVC', 'Covenant Church'), ('EL', 'Episcopal'), ('EVF', 'Evangelical Free'), ('IP', 'Independent Pentecostal'), ('LN', 'Lutheran'), ('ME', 'Menonite'), ('MT', 'Methodist'), ('NZ', 'Nazarene'), ('PB', 'Presbyterian'), ('RD', 'Reformed'), ('WN', 'Wesleyan'), ('OTR', 'Other')], default='OTR', max_length=3),
            preserve_default=False,
        ),
    ]
