from django.forms import ModelForm, Form, EmailField, CharField
from students.models import Student

class StudentsAddForm(ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

class StudentsAddForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data
        # Пишем отправку письма