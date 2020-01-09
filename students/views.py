from django.shortcuts import render
# Create your views here.
from students.models import Student
from django.http import HttpResponse, HttpResponseRedirect


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
    from students.forms import StudentsAddForm

    if request.method == 'POST':

        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

    else:
        form = StudentsAddForm()

    return render(request, 'students_add.html', context={"form": form})
