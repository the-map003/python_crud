from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Student
from .forms import StudentForm


# CREATE - Display form and handle student creation
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'crud_app/student_form.html', {'form': form, 'action': 'Create'})


# RETRIEVE - Display all students (List view)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'crud_app/student_list.html', {'students': students})


# RETRIEVE - Display single student (Detail view)
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'crud_app/student_detail.html', {'student': student})


# UPDATE - Display form and handle student update
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'crud_app/student_form.html', {'form': form, 'action': 'Update', 'student': student})


# DELETE - Display confirmation and handle student deletion
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'crud_app/student_confirm_delete.html', {'student': student})
