# Generated by Django 4.2.2 on 2023-06-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.news'),
        ),
    ]
