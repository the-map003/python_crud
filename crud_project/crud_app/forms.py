from django import forms

from . models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "registration_number",
            "course",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "email@example.com"}),
            "registration_number": forms.TextInput(
                attrs={"placeholder": "e.g. REG-2026-001"}
            ),
            "course": forms.TextInput(attrs={"placeholder": "Course name"}),
        }
