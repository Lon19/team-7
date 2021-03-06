# Generated by Django 2.2.6 on 2019-11-02 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20191102_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertype',
            name='questionTypeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.QuestionType'),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.QuestionType'),
        ),
    ]
