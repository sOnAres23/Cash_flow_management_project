from django import forms
from .models import Record, Category, Subcategory, Type, Status


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
        if self.instance and self.instance.type:
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type)
            if self.instance.category:
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)

        # Динамическая фильтрация подкатегорий по выбранной категории
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance and self.instance.category:
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category)

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Сумма должна быть больше нуля.")
        return amount


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
