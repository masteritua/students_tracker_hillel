from django.shortcuts import render
# Create your views here.
from students.models import Student
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from students.forms import StudentsAddForm

def students(request):
    queryset = Student.objects.all()
    response = ""

    fn = request.GET.get('first_name')

    if fn:
        pass
        # LIKE %{}%
        # queryset.filter(first_name__contains=fn)

        # LIKE %{}
        # queryset.filter(first_name__endswith=fn)

        # LIKE {}%
        # queryset.filter(first_name__startswith=fn)

    for student in queryset:
        response += student.get_info() + "<br>"

    return render(request, 'students_list.html', context={'students_list': response})


def students_add(request):

    if request.method == 'POST':

        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('/students'))

    else:
        form = StudentsAddForm()

    return render(request, 'students_add.html', context={"form": form})


def students_edit(request, pk):

    try:
        pass
    except Student.DoesNotExist:
        return HttpResponseNotFound(f'Students with id {pk} not found')


    if request.method == 'POST':

        form = StudentsAddForm(request.POST, instance=students)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('/students'))

    else:
        form = StudentsAddForm(request.POST, instance=students)

    return render(request,
                  'students_edit.html',
                  context={
                      "form": form,
                      'pk':pk
                  })

def contact():

    if request.method == 'POST':

        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('/students'))

    else:
        form = StudentsAddForm()

    return render(request, 'students_add.html', context={"form": form})
