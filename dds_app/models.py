from django.db import models


class Type(models.Model):
    """Вспомогательный класс для типов записи о движении денежных средств (ДДС)"""

    TYPE_CHOICES = [
        ('Пополнение', 'пополнение'),
        ('Списание', 'списание'),
    ]

    name = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Status(models.Model):
    """Вспомогательный класс для статусов записи о движении денежных средств (ДДС)"""

    STATUS_CHOICES = [
        ('Бизнес', 'бизнес'),
        ('Личное', 'личное'),
        ('Налог', 'налог'),
    ]

    name = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Category(models.Model):
    """
    Класс для категорий, к которым могут быть привязаны записи о движении денежных средств.

    Каждая категория привязана к определенному типу записи.
    """
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    """
    Класс для подкатегорий, которые относятся к определенной категории.

    Каждая подкатегория привязана к категории, и может быть выбрана только в том случае,
    если категория уже выбрана в записи о движении денежных средств.
    """
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Record(models.Model):
    """
    Класс для записи о движении денежных средств (ДДС).

    Каждая запись отражает:
    - Дата создания записи (date)
    - Статус (status)
    - Тип (type)
    - Категория (category)
    - Подкатегория (subcategory)
    - Сумма (amount)
    - Комментарий (comment)

    Записи могут быть связаны с различными категориями и подкатегориями, которые в свою очередь
    должны быть привязаны к типу записи.
    """
    date = models.DateField(auto_now_add=True, verbose_name="Дата записи")
    status = models.ForeignKey(Status, related_name='records', on_delete=models.CASCADE, verbose_name="Статус записи")
    type = models.ForeignKey(Type, related_name='records', on_delete=models.CASCADE, verbose_name="Тип записи")
    category = models.ForeignKey(Category, related_name='records', on_delete=models.CASCADE,
                                 verbose_name="Категория записи")
    subcategory = models.ForeignKey(Subcategory, related_name='records', on_delete=models.CASCADE,
                                    verbose_name="Подкатегория записи")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма в рублях")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий (необязательное поле)")

    def __str__(self):
        return f'{self.date} - {self.status.get_name_display()} - {self.type.get_name_display()}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
