# Student Registration CRUD System

A comprehensive Django-based CRUD (Create, Read, Update, Delete) application for managing student registrations. Perfect for teaching web development concepts.

## Overview

This application demonstrates all four CRUD operations using a student registration form as an example:

- **Create (C)**: Register new students with their information
- **Read/Retrieve (R)**: View all students in a list or view individual student details
- **Update (U)**: Edit existing student information
- **Delete (D)**: Remove students from the system

## Project Structure

```
crud_project/
├── manage.py
├── db.sqlite3
├── crud_app/
│   ├── models.py          # Student model definition
│   ├── views.py           # CRUD view functions
│   ├── forms.py           # StudentForm for data validation
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Django admin configuration
│   └── migrations/        # Database migrations
└── crud_project/
    ├── settings.py        # Django settings
    ├── urls.py            # Main URL configuration
    ├── wsgi.py
    └── asgi.py
templates/
├── base.html              # Base template with navbar
└── crud_app/
    ├── student_list.html        # Display all students
    ├── student_detail.html      # View single student
    ├── student_form.html        # Create/Update form
    └── student_confirm_delete.html  # Delete confirmation
```

## Model: Student

The Student model includes the following fields:

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key (auto-generated) |
| first_name | String | Student's first name (max 100 chars) |
| last_name | String | Student's last name (max 100 chars) |
| email | Email | Unique email address |
| roll_number | String | Unique student ID (max 20 chars) |
| phone | String | Contact number (max 15 chars) |
| date_of_birth | Date | Student's birth date (optional) |
| address | Text | Residential address (optional) |
| enrollment_date | Date | Automatically set to registration date |

## CRUD Operations

### 1. CREATE - Register a New Student
**Endpoint**: `/students/create/`
- Display registration form
- Validate input data
- Save new student to database
- Redirect to student list

**Views Function**: `student_create()`

### 2. READ/RETRIEVE - View Students
**List All Students**:
- Endpoint: `/students/`
- Display all registered students in a table
- Show student count
- Display action buttons

**View Single Student**:
- Endpoint: `/students/<id>/`
- Display complete student details
- Show all fields including optional ones
- Provide edit and delete options

**Views Functions**: `student_list()`, `student_detail()`

### 3. UPDATE - Edit Student Information
**Endpoint**: `/students/<id>/update/`
- Pre-fill form with existing data
- Allow modification of all fields except enrollment_date
- Validate changes
- Save updates to database
- Redirect to student detail view

**Views Function**: `student_update()`

### 4. DELETE - Remove Student
**Endpoint**: `/students/<id>/delete/`
- Display student information for confirmation
- Prevent accidental deletion with confirmation page
- Permanently remove from database on confirmation
- Redirect to student list

**Views Function**: `student_delete()`

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 6.0.2

### Steps

1. **Install Django** (if not already installed):
   ```bash
   pip install django
   ```

2. **Navigate to project directory**:
   ```bash
   cd crud_project
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create superuser** (for admin panel):
   ```bash
   python manage.py createsuperuser
   ```

5. **Start development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Student CRUD: http://localhost:8000/students/
   - Admin Panel: http://localhost:8000/admin/

## URLs Reference

| Operation | URL | HTTP Method |
|-----------|-----|-------------|
| List Students | `/students/` | GET |
| Create Student | `/students/create/` | GET, POST |
| View Student | `/students/<id>/` | GET |
| Update Student | `/students/<id>/update/` | GET, POST |
| Delete Student | `/students/<id>/delete/` | GET, POST |
| Admin Panel | `/admin/` | GET, POST |

## Features

✅ **User-Friendly Interface**
- Responsive Bootstrap 5 design
- Mobile-friendly layout
- Intuitive navigation

✅ **Data Validation**
- Email uniqueness validation
- Roll number uniqueness validation
- Required field validation
- Form error display

✅ **Admin Panel Integration**
- Manage students from Django admin
- Filter by enrollment date
- Search by name, email, or roll number

✅ **Educational Features**
- Clean code structure for learning
- Commented CRUD operations
- Proper use of Django best practices
- Template inheritance for code reuse

## Teaching Points

This project can be used to teach:

1. **Django Models**: Database design and ORM
2. **Views**: Function-based views for CRUD operations
3. **Forms**: Django ModelForm for data validation
4. **Templates**: Template inheritance and rendering
5. **URL Routing**: URL patterns and namespacing
6. **HTTP Methods**: GET vs POST requests
7. **Database Operations**: CRUD via ORM
8. **Admin Interface**: Django admin customization
9. **HTML Forms**: Form submission and validation
10. **Responsive Design**: Bootstrap integration

## Sample Code Snippets

### Create View
```python
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'crud_app/student_form.html', 
                  {'form': form, 'action': 'Create'})
```

### Update View
```python
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'crud_app/student_form.html', 
                  {'form': form, 'action': 'Update'})
```

### Delete View
```python
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'crud_app/student_confirm_delete.html', 
                  {'student': student})
```

## Customization

### Adding More Fields
1. Modify the `Student` model in `models.py`
2. Add field to `StudentForm` in `forms.py`
3. Run `python manage.py makemigrations`
4. Run `python manage.py migrate`
5. Update templates to display the new field

### Styling
- Bootstrap 5 is already included via CDN
- Modify `templates/base.html` to change the color scheme
- The gradient colors are defined in the `<style>` section

## Troubleshooting

**Issue**: Page shows "student_list not found"
**Solution**: Ensure URLs are properly configured in `crud_app/urls.py` and included in main `urls.py`

**Issue**: Form doesn't save data
**Solution**: Check that `CSRF token` is included in form and all required fields have values

**Issue**: Database errors
**Solution**: Run `python manage.py migrate` to ensure all migrations are applied

## Future Enhancements

- Add student photo upload
- Add grades/marks management
- Add attendance tracking
- Add email notifications
- Add batch operations (import/export)
- Add user authentication and permissions
- Add pagination for large student lists
- Add search and advanced filtering

## License

This project is open source and available for educational purposes.

## Author

Created for teaching CRUD operations with Django.

---

**Happy Teaching! 🎓**