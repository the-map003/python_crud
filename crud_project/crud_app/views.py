from django.shortcuts import get_object_or_404, redirect, render

from .models import Student


def student_list(request):
    students = Student.objects.order_by("-created_at")
    return render(request, "crud_app/student_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        Student.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            registration_number=request.POST.get("registration_number"),
            course=request.POST.get("course"),
        )
        return redirect("student_list")

    return render(request,"crud_app/student_create.html",
        {
            "page_heading": "Register Student",
            "page_subtitle": "Insert a new student record into the registry.",
        },
    )


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.email = request.POST.get("email")
        student.registration_number = request.POST.get("registration_number")
        student.course = request.POST.get("course")
        student.save()
        return redirect("student_list")

    return render(request,"crud_app/student_update.html",
        {
            "student": student,
            "page_heading": "Update Student",
            "page_subtitle": "Edit an existing student record.",
        },
    )


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request,"crud_app/student_confirm_delete.html",
        {
            "student": student,
            "page_heading": "Delete Student",
            "page_subtitle": "Remove a student record from the registry. This action cannot be undone.",
        },
    )
