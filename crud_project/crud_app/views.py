from django.shortcuts import get_object_or_404, redirect, render

from . forms import StudentForm
from . models import Student


def student_list(request):
	students = Student.objects.order_by("-created_at")
	return render(request, "crud_app/student_list.html", {"students": students})


def student_create(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("student_list")
	else:
		form = StudentForm()

	return render(
		request,
		"crud_app/student_form.html",
		{"form": form, "title": "Register Student"},
	)


def student_update(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == "POST":
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect("student_list")
	else:
		form = StudentForm(instance=student)

	return render(
		request,
		"crud_app/student_form.html",
		{"form": form, "title": "Update Student"},
	)


def student_delete(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == "POST":
		student.delete()
		return redirect("student_list")

	return render(
		request,
		"crud_app/student_confirm_delete.html",
		{"student": student},
	)
