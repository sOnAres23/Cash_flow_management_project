from django import forms
from .models import Record, Category, Subcategory, Type, Status
from .services import validate_category_and_subcategory


class RecordForm(forms.ModelForm):
    """Форма для создания и редактирования записи о движении денежных средств (ДДС)"""

    class Meta:
        model = Record
        fields = ['status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Динамическая фильтрация категорий по выбранному типу
        if self.instance and self.instance.pk:  # Проверяем, что instance существует и это не новая запись
            if self.instance.type:
                # Если тип записи существует, фильтруем категории по этому типу
                self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)
                if self.instance.category:
                    # Если категория уже выбрана, фильтруем подкатегории по этой категории
                    self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)

        # Фильтрация подкатегорий по категории при редактировании
        if 'category' in self.data:
            category_id = int(self.data.get('category'))
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
        elif self.instance and self.instance.pk:
            if self.instance.category:
                # Проверяем, что у instance есть категория, чтобы фильтровать подкатегории
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)

        # Если тип еще не выбран, фильтруем категории по всем типам
        if self.instance and self.instance.pk:
            if not self.instance.type:
                self.fields['category'].queryset = Category.objects.all()

    def clean_amount(self):
        """Проверка суммы на корректность"""
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Сумма должна быть больше нуля.")
        return amount

    def clean(self):
        """Проверка на зависимость категории с типом и подкатегории"""
        cleaned_data = super().clean()

        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        record_type = cleaned_data.get('type')

        # Вызов валидации "Бизнес-правила" из services.py
        validate_category_and_subcategory(category, subcategory, record_type)

        return cleaned_data


class CategoryForm(forms.ModelForm):
    """Форма для создания и редактирования категории. Каждая категория привязана к типу"""

    class Meta:
        model = Category
        fields = ['name', 'type']


class SubcategoryForm(forms.ModelForm):
    """Форма для создания и редактирования подкатегории. Каждая подкатегория привязана к категории"""

    class Meta:
        model = Subcategory
        fields = ['name', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['category'].queryset = Category.objects.filter(id=category_id)
            except (ValueError, TypeError):
                pass


class TypeForm(forms.ModelForm):
    """Форма для создания и редактирования типа записи"""

    class Meta:
        model = Type
        fields = ['name']


class StatusForm(forms.ModelForm):
    """Форма для создания и редактирования статуса записи"""

    class Meta:
        model = Status
        fields = ['name']
