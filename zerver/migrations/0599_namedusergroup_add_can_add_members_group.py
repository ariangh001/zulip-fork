# Generated by Django 5.0.9 on 2024-10-07 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0598_alter_namedusergroup_can_join_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="namedusergroup",
            name="can_add_members_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]
