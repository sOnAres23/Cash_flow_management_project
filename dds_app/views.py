from django.shortcuts import render, redirect, get_object_or_404
from .models import Record, Category, Subcategory, Type, Status
from .forms import RecordForm, CategoryForm, SubcategoryForm, TypeForm, StatusForm


def record_list(request):
    """Представление для отображения списка всех записей о движении денежных средств.
    Поддерживает фильтрацию по дате, статусу, типу, категории и подкатегории.
    """
    records = Record.objects.all()

    # Фильтрация по дате
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])

    # Фильтрация по статусу
    status = request.GET.get('status')
    if status:
        records = records.filter(status=status)

    # Фильтрация по типу
    record_type = request.GET.get('type')
    if record_type:
        records = records.filter(type__name=record_type)

    # Фильтрация по категории
    category = request.GET.get('category')
    if category:
        records = records.filter(category__name=category)

    # Фильтрация по подкатегории
    subcategory = request.GET.get('subcategory')
    if subcategory:
        records = records.filter(subcategory__name=subcategory)

    return render(request, 'record_list.html', {'records': records})


def record_edit(request, pk):
    """
    Представление для редактирования существующей записи о движении денежных средств.
    """
    record = get_object_or_404(Record, pk=pk)

    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'record_form.html', {'form': form})


def record_create(request):
    """
    Представление для создания новой записи о движении денежных средств.
    """
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = RecordForm()
    return render(request, 'record_form.html', {'form': form})


def record_delete(request, pk):
    """
    Представление для удаления записи о движении денежных средств.
    """
    record = get_object_or_404(Record, pk=pk)
    record.delete()
    return redirect('record_list')


def category_edit(request, pk=None):
    """
    Представление для создания или редактирования категории.
    Если pk передан, то редактируем существующую категорию.
    """
    if pk:
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST or None, instance=category)
    else:
        form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('category_list')

    return render(request, 'category_form.html', {'form': form})


def subcategory_edit(request, pk=None):
    """
    Представление для создания или редактирования подкатегории.
    """
    if pk:
        subcategory = get_object_or_404(Subcategory, pk=pk)
        form = SubcategoryForm(request.POST or None, instance=subcategory)
    else:
        form = SubcategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('subcategory_list')

    return render(request, 'subcategory_form.html', {'form': form})


def type_edit(request, pk=None):
    """
    Представление для создания или редактирования типа.
    """
    if pk:
        type_obj = get_object_or_404(Type, pk=pk)
        form = TypeForm(request.POST or None, instance=type_obj)
    else:
        form = TypeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('type_list')

    return render(request, 'type_form.html', {'form': form})


def status_edit(request, pk=None):
    """
    Представление для создания или редактирования статуса.
    """
    if pk:
        status_obj = get_object_or_404(Status, pk=pk)
        form = StatusForm(request.POST or None, instance=status_obj)
    else:
        form = StatusForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('status_list')

    return render(request, 'status_form.html', {'form': form})
