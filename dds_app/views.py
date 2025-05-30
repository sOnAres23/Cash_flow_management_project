from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Record, Category, Subcategory, Type, Status
from .forms import RecordForm, CategoryForm, SubcategoryForm, TypeForm, StatusForm


class RecordListView(ListView):
    """
    Представление для отображения списка записей о движении денежных средств (ДДС).
    Поддержка фильтрации по дате, статусу, типу, категории и подкатегории.
    """
    model = Record
    template_name = 'dds_app/record_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Фильтрация по дате
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        # Фильтрация по статусу
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        # Фильтрация по типу
        type = self.request.GET.get('type')
        if type:
            queryset = queryset.filter(type__name=type)

        # Фильтрация по категории
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__name=category)

        # Фильтрация по подкатегории
        subcategory = self.request.GET.get('subcategory')
        if subcategory:
            queryset = queryset.filter(subcategory__name=subcategory)

        return queryset


class RecordCreateView(CreateView):
    """
    Представление для создания новой записи о движении денежных средств (ДДС).
    """
    model = Record
    form_class = RecordForm
    template_name = 'dds_app/record_form.html'
    success_url = reverse_lazy('record_list')

    def form_valid(self, form):
        # Можно добавить дополнительные действия перед сохранением формы
        return super().form_valid(form)


class RecordUpdateView(UpdateView):
    """
    Представление для редактирования существующей записи о движении денежных средств (ДДС).
    """
    model = Record
    form_class = RecordForm
    template_name = 'dds_app/record_form.html'
    success_url = reverse_lazy('record_list')

    def form_valid(self, form):
        return super().form_valid(form)


class RecordDeleteView(DeleteView):
    """
    Представление для удаления записи о движении денежных средств (ДДС).
    """
    model = Record
    template_name = 'dds_app/record_confirm_delete.html'
    success_url = reverse_lazy('record_list')


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    """
    Представление для создания новой категории.
    """
    model = Category
    form_class = CategoryForm
    template_name = 'dds_app/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    """
    Представление для редактирования существующей категории.
    """
    model = Category
    form_class = CategoryForm
    template_name = 'dds_app/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    """
    Представление для удаления категории.
    """
    model = Category
    template_name = 'dds_app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class SubcategoryListView(ListView):
    model = Subcategory
    template_name = 'subcategory_list.html'
    context_object_name = 'subcategories'


class SubcategoryCreateView(CreateView):
    """
    Представление для создания новой подкатегории.
    """
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'dds_app/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')


class SubcategoryUpdateView(UpdateView):
    """
    Представление для редактирования существующей подкатегории.
    """
    model = Subcategory
    form_class = SubcategoryForm
    template_name = 'dds_app/subcategory_form.html'
    success_url = reverse_lazy('subcategory_list')


class SubcategoryDeleteView(DeleteView):
    """
    Представление для удаления подкатегории.
    """
    model = Subcategory
    template_name = 'dds_app/subcategory_confirm_delete.html'
    success_url = reverse_lazy('subcategory_list')


class TypeListView(ListView):
    model = Type
    template_name = 'type_list.html'
    context_object_name = 'types'


class TypeCreateView(CreateView):
    """
    Представление для создания нового типа записи.
    """
    model = Type
    form_class = TypeForm
    template_name = 'dds_app/type_form.html'
    success_url = reverse_lazy('type_list')


class TypeUpdateView(UpdateView):
    """
    Представление для редактирования существующего типа записи.
    """
    model = Type
    form_class = TypeForm
    template_name = 'dds_app/type_form.html'
    success_url = reverse_lazy('type_list')


class TypeDeleteView(DeleteView):
    """
    Представление для удаления типа записи.
    """
    model = Type
    template_name = 'dds_app/type_confirm_delete.html'
    success_url = reverse_lazy('type_list')


class StatusListView(ListView):
    model = Status
    template_name = 'status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(CreateView):
    """
    Представление для создания нового статуса.
    """
    model = Status
    form_class = StatusForm
    template_name = 'dds_app/status_form.html'
    success_url = reverse_lazy('status_list')


class StatusUpdateView(UpdateView):
    """
    Представление для редактирования существующего статуса.
    """
    model = Status
    form_class = StatusForm
    template_name = 'dds_app/status_form.html'
    success_url = reverse_lazy('status_list')


class StatusDeleteView(DeleteView):
    """
    Представление для удаления статуса.
    """
    model = Status
    template_name = 'dds_app/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')

