from django.db import models

class Todolist(models.Model):
    """Список задач"""
    id = models.AutoField(primary_key=True)
    description = models.TextField("Описание")
    status = models.BooleanField('Выполнено')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"