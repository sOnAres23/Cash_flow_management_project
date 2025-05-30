from django.core.exceptions import ValidationError


def validate_category_and_subcategory(category, subcategory, record_type):
    """Проверка на зависимость категории с типом и подкатегории"""

    # Проверка на зависимость категории и типа
    if category and record_type:
        if category.type != record_type:
            raise ValidationError('Категория должна относиться к выбранному типу.')

    # Проверка на зависимость подкатегории и категории
    if subcategory and category:
        if subcategory.category != category:
            raise ValidationError('Подкатегория должна быть связана с выбранной категорией.')
