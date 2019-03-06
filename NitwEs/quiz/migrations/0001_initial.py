# Generated by Django 2.1.7 on 2019-03-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('op1', models.TextField()),
                ('op2', models.TextField()),
                ('op3', models.TextField()),
                ('op4', models.TextField()),
                ('answer', models.CharField(choices=[('op1', 'option1'), ('op2', 'option2'), ('op3', 'option3'), ('op4', 'option4')], max_length=10)),
            ],
        ),
    ]
