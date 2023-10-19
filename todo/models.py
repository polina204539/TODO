from django.db import models

class Todolist(models.Model):
    """Список задач"""
    id = models.AutoField(primary_key=True)
    description = models.TextField("Описание")
    status = models.ForeignKey('Status', on_delete=models.PROTECT)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

class Status(models.Model):
    """Статус"""
    id = models.AutoField(primary_key=True)
    name = models.TextField("Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"  