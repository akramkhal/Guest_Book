from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Guest(models.Model):
    author_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Имя")
    author_email = models.EmailField(max_length=100, null=False, blank=False, verbose_name="Почта")
    text = models.TextField(null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Статус")

    def __str__(self):
        return f'{self.author_name} - {self.author_email}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

