from django.db import models

class Category(models.Model):
    title = models.CharField('Название категории', max_length=200)

class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=290)
    is_complete = models.BooleanField('Завершение', default=False)


    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title