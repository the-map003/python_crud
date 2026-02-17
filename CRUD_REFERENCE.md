# CRUD Operations - Quick Reference Guide

## What is CRUD?

CRUD stands for the four basic operations on data:
- **C** - CREATE: Add new data (INSERT)
- **R** - READ/RETRIEVE: View existing data (SELECT)
- **U** - UPDATE: Modify existing data (UPDATE)
- **D** - DELETE: Remove data (DELETE)

## In This Student Registration System

### 1️⃣ CREATE - Register a New Student

**When to use**: When adding a new student to the system

**URL**: `http://localhost:8000/students/create/`

**Steps**:
1. Click "➕ Add New Student" button
2. Fill in all required fields (marked with *)
3. Click "✅ Register Student"
4. You'll be redirected to the student list

**What happens**: 
- Form data is validated
- New Student record is created in database
- User is redirected to the student list view

**Code Location**: `crud_app/views.py` → `student_create()` function

---

### 2️⃣ READ/RETRIEVE - View Student Data

**When to use**: When you want to look at student information

**Two types:**

#### A. View All Students (List View)
- **URL**: `http://localhost:8000/students/`
- **Shows**: Table of all registered students
- **Information**: Roll number, name, email, phone, enrollment date
- **Code Location**: `crud_app/views.py` → `student_list()` function

#### B. View Single Student (Detail View)
- **URL**: `http://localhost:8000/students/<id>/`
- **Shows**: Complete student details
- **Information**: All fields including address, date of birth
- **Code Location**: `crud_app/views.py` → `student_detail()` function

---

### 3️⃣ UPDATE - Edit Student Information

**When to use**: When you need to modify a student's details

**URL**: `http://localhost:8000/students/<id>/update/`

**Steps**:
1. Click "✏️ Edit" button next to a student
2. Modify the fields you want to change
3. Click "💾 Save Changes"
4. You'll see the updated student details

**What happens**:
- Form is pre-filled with existing data
- Changes are validated
- Database is updated with new information
- User is redirected to student detail view

**Code Location**: `crud_app/views.py` → `student_update()` function

---

### 4️⃣ DELETE - Remove a Student

**When to use**: When removing a student from the system

**URL**: `http://localhost:8000/students/<id>/delete/`

**Steps**:
1. Click "🗑️ Delete" button next to a student
2. Review the student information on confirmation page
3. Click "🗑️ Yes, Delete Student" to confirm
4. Student is permanently removed
5. You're redirected to the student list

**⚠️ Warning**: This action cannot be undone!

**Code Location**: `crud_app/views.py` → `student_delete()` function

---

## Database Fields Explained

| Field | Editable | Auto-filled | Description |
|-------|----------|------------|-------------|
| Roll Number | ✅ Yes | ❌ No | Student's unique ID |
| First Name | ✅ Yes | ❌ No | Student's first name |
| Last Name | ✅ Yes | ❌ No | Student's last name |
| Email | ✅ Yes | ❌ No | Student's email (must be unique) |
| Phone | ✅ Yes | ❌ No | Student's contact number |
| Date of Birth | ✅ Yes | ❌ No | Optional: Student's birthday |
| Address | ✅ Yes | ❌ No | Optional: Residential address |
| Enrollment Date | ❌ No | ✅ Yes | Auto-set when student is registered |
| ID | ❌ No | ✅ Yes | Auto-generated unique identifier |

---

## Key Concepts

### Model
- File: `crud_app/models.py`
- Defines the Student data structure
- Maps to database table

### View
- File: `crud_app/views.py`
- Contains business logic for CRUD operations
- Handles form processing
- Renders templates with data

### Form
- File: `crud_app/forms.py`
- Validates user input
- Handles data transformation
- Generates HTML form from model

### Template
- Files in: `templates/crud_app/`
- HTML pages displayed to users
- Receives data from views
- Shows forms and student information

### URL Routing
- File: `crud_app/urls.py` (app URLs) & `crud_project/urls.py` (main URLs)
- Maps URLs to views
- Example: `/students/create/` → `student_create()` view

---

## Common Scenarios

### Scenario 1: Add a student
1. Go to `/students/create/`
2. Fill form → Click "Register" → **CREATE** complete

### Scenario 2: Check student details
1. Go to `/students/` → Click "View" → **READ** complete

### Scenario 3: Correct a student's email
1. Go to `/students/<id>/update/`
2. Change email → Click "Save" → **UPDATE** complete

### Scenario 4: Remove a student
1. Go to `/students/<id>/delete/`
2. Confirm deletion → **DELETE** complete

---

## SQL Equivalent

For those familiar with SQL, here's what happens under the hood:

```sql
-- CREATE
INSERT INTO crud_app_student (first_name, last_name, email, roll_number, phone, ...) 
VALUES ('Rajesh', 'Kumar', 'rajesh@example.com', 'CSE001', '9876543210', ...);

-- READ (List)
SELECT * FROM crud_app_student;

-- READ (Detail)
SELECT * FROM crud_app_student WHERE id = 1;

-- UPDATE
UPDATE crud_app_student 
SET email = 'newemail@example.com' 
WHERE id = 1;

-- DELETE
DELETE FROM crud_app_student WHERE id = 1;
```

---

## Tips for Demonstration

✅ **Do this:**
- Show how forms validate data (e.g., duplicate email error)
- Demonstrate all four operations in order
- Compare creation and update forms
- Show the confirmation page before deletion

❌ **Don't do this:**
- Delete all students – keep sample data for reference
- Edit read-only fields (enrollment_date)
- Skip the confirmation page for deletion

---

## Troubleshooting

**Q: Form shows error but I'm sure the data is correct**
- A: Check special characters, spaces, or formatting issues

**Q: Can't find "Update" button**
- A: Make sure you're on the student detail page first

**Q: Student was deleted accidentally**
- A: Check the database backups (restoring is outside Django)

**Q: Email field shows "already exists" error**
- A: This is a constraint - each student must have a unique email

---

## Advanced Topics (Optional)

- Model relationships (Foreign Keys)
- QuerySets and filtering
- Custom validators
- Pagination for large datasets
- Search and filtering
- Bulk operations
- API creation with Django REST Framework

---

Happy Learning! 📚
