# Generated by Django 4.2.9 on 2024-02-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0058_remoteinstallationcount_add_mobile_pushes_forwarded_index"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="remoterealmauditlog",
            index=models.Index(
                condition=models.Q(("event_type__in", [101, 102, 103, 104, 105, 201, 202, 229])),
                fields=["remote_realm_id", "id"],
                name="zilencer_remoterealmauditlog_synced_billing_events",
            ),
        ),
    ]
