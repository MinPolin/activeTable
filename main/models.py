from django.db import models

class Data(models.Model):
    base_id = models.CharField(max_length=64,default='')
    fon_id = models.CharField(max_length=200,default='')
    time = models.DateTimeField(auto_now_add=True, auto_now=False)
    error_text = models.TextField(default='')
    STATUS = (
        ('w', 'Ожидает отправки'),
        ('d', 'Отправлен'),
        ('s', 'Успешно сохранен'),
        ('e', 'Ошибка'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=False,
        default='w',
        help_text='Статус записи')

    def __str__(self):
        return self.base_id

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Хранилище записей"
