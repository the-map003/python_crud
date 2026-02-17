# ✅ Pre-Class Verification Checklist

Use this checklist to verify everything is working before teaching!

---

## 🔧 Setup Verification (Before First Class)

### Step 1: Project Structure
```bash
cd d:\Projects\Jerome\python_crud\crud_project
```

**Verify these files exist:**
- [ ] `manage.py` - Django management script
- [ ] `db.sqlite3` - Database file
- [ ] `crud_app/models.py` - Student model
- [ ] `crud_app/views.py` - CRUD views
- [ ] `crud_app/forms.py` - Student form
- [ ] `crud_app/urls.py` - App URLs
- [ ] `crud_project/urls.py` - Main URLs
- [ ] `crud_project/settings.py` - Django settings

### Step 2: Templates
**Verify templates directory exists:**
```bash
templates/
├── base.html
└── crud_app/
    ├── student_list.html
    ├── student_detail.html
    ├── student_form.html
    └── student_confirm_delete.html
```

- [ ] Base template exists
- [ ] All 4 app templates exist
- [ ] Bootstrap styling is included

### Step 3: Database
**Verify database is set up:**
```bash
python manage.py check
```

Expected output:
```
System check identified no issues (0 silenced).
```

**Run migrations if not done:**
```bash
python manage.py migrate
```

- [ ] No errors from `python manage.py check`
- [ ] Database file exists and is > 50KB
- [ ] Migrations have been applied

---

## 🚀 Functionality Testing

### Step 4: Start Server
```bash
python manage.py runserver
```

Expected output:
```
Starting development server at http://127.0.0.1:8000/
```

- [ ] Server starts without errors
- [ ] No port 8000 conflict

### Step 5: Test Student List (READ)
**URL:** http://localhost:8000/students/

✅ **Expected:**
- [ ] Page loads without errors
- [ ] Shows "No students found" message
- [ ] "➕ Add New Student" button is visible
- [ ] Navigation bar is present
- [ ] Page is styled (not plain HTML)

❌ **If broken:**
- Check templates are in right location
- Check Bootstrap CDN is loading
- Run `python manage.py check`

### Step 6: Test Create Form (CREATE)
**URL:** http://localhost:8000/students/create/

✅ **Expected:**
- [ ] Form loads with all fields
- [ ] Fields are: First Name, Last Name, Email, Roll Number, Phone, DOB, Address
- [ ] "Register Student" button is visible
- [ ] Form has proper styling

✅ **Try submitting empty form:**
- [ ] Shows validation errors
- [ ] Fields are highlighted
- [ ] Error messages are clear

✅ **Fill out correctly:**
- [ ] Roll Number: `TEST001`
- [ ] First Name: `John`
- [ ] Last Name: `Doe`
- [ ] Email: `john@testexample.com`
- [ ] Phone: `9876543210`

✅ **Submit form:**
- [ ] Form validates successfully
- [ ] Page redirects to student list (after 1-2 seconds)
- [ ] New student appears in list

❌ **If broken:**
- Check forms.py exists
- Check models.py has Student class
- Check migrations have been applied

### Step 7: Test Student Detail (READ)
**URL:** http://localhost:8000/students/1/

✅ **Expected:**
- [ ] Shows the student you just created
- [ ] All fields are displayed
- [ ] Edit and Delete buttons are visible
- [ ] Correct data is shown

❌ **If broken:**
- Check the URL has the correct student ID
- Check student_detail.html template exists

### Step 8: Test Update (UPDATE)
**On the detail page, click "✏️ Edit"**

✅ **Expected:**
- [ ] Form loads with pre-filled data
- [ ] Current email is shown in email field
- [ ] Phone number is shown in phone field
- [ ] Button says "💾 Save Changes" (not "Register Student")

✅ **Update email:**
- [ ] Clear email field
- [ ] Enter: `john.updated@testexample.com`
- [ ] Click "Save Changes"
- [ ] Redirects to detail page
- [ ] Email is updated

❌ **If broken:**
- Check student_update() function in views.py
- Check instance parameter in form
- Check URL pattern includes ID

### Step 9: Test Delete (DELETE)
**On the detail page, click "🗑️ Delete"**

✅ **Expected:**
- [ ] Confirmation page loads
- [ ] Shows student name and details
- [ ] Shows warning message
- [ ] "🗑️ Yes, Delete Student" button is visible
- [ ] "❌ Cancel" button is visible

✅ **Confirm deletion:**
- [ ] Click "Yes, Delete Student"
- [ ] Redirects to student list
- [ ] Student is no longer in list

❌ **If broken:**
- Check student_delete() function
- Check student_confirm_delete.html template
- Verify POST method handling

### Step 10: Test Admin Panel
**URL:** http://localhost:8000/admin/

✅ **Expected:**
- [ ] Login page appears
- [ ] Login with your superuser credentials
- [ ] Django admin loads
- [ ] "Student" model is visible in admin
- [ ] Can see CRUD operations in admin

---

## 📊 Advanced Checks

### Step 11: Sample Data
**Load sample data:**
```bash
python manage.py shell
exec(open('sample_data.py').read())
exit()
```

✅ **Expected:**
- [ ] Command runs without errors
- [ ] Shows "✅ Created" messages
- [ ] Shows "📊 Summary: X created"

**Verify data:**
- [ ] Go to http://localhost:8000/students/
- [ ] See 8 sample students (or more if run before)

### Step 12: Search and Filter
**In admin panel:**
- [ ] Click "Student" in admin
- [ ] Try searching for a name
- [ ] Try filtering by enrollment_date
- [ ] Verify correct results

### Step 13: Database Query
**In Django shell:**
```bash
python manage.py shell
```

```python
from crud_app.models import Student

# Test queries
count = Student.objects.count()
print(f"Total students: {count}")

# Get one
student = Student.objects.first()
print(f"First student: {student}")

# Get all
all_students = Student.objects.all()
for s in all_students:
    print(f"  - {s.roll_number}: {s.first_name} {s.last_name}")
```

✅ **Expected:**
- [ ] No errors
- [ ] Shows correct count
- [ ] Lists students properly

---

## 🎓 Teaching Preparation Checklist

### Documentation
- [ ] Read `GETTING_STARTED.md`
- [ ] Review `TEACHING_PLAN.md` Session 1
- [ ] Have `CRUD_REFERENCE.md` ready for students
- [ ] Bookmark all documentation files

### Test Scenarios Prepared
- [ ] Create a test student
- [ ] Navigate through all pages
- [ ] Show database query in shell
- [ ] Show admin panel

### Demo Data
- [ ] Sample data loaded (8 students)
- [ ] One test student for live demo
- [ ] Ready to create new during class

### Environment Ready
- [ ] Server can start reliably
- [ ] No port conflicts
- [ ] All pages render correctly
- [ ] No JavaScript errors (check browser console)

### Files Prepared
- [ ] Documentation printed or bookmarked
- [ ] Sample code available
- [ ] Database backup (if needed)
- [ ] Teaching notes ready

---

## 🔍 Troubleshooting Quick Guide

### "Page not found (404)"
```bash
# Solution:
python manage.py check
python manage.py migrate
# Restart server
```

### "Connection refused"
```bash
# Solution: Port 8000 is in use
python manage.py runserver 8001  # Use different port
```

### "Database is locked"
```bash
# Solution: Stop server, delete db.sqlite3, restart
python manage.py migrate
```

### "No module named 'django'"
```bash
# Solution: Install Django
pip install django==6.0.2
```

### "Template not found"
```bash
# Solution: Check:
# 1. Templates directory exists: templates/crud_app/
# 2. DIRS is set in settings.py
# 3. APP_DIRS is True in settings.py
```

### "Form not rendering"
```bash
# Solution: Check forms.py exists and StudentForm class is defined
# Verify all fields are listed in Meta.fields
```

---

## 📱 Browser Compatibility

**Test in multiple browsers:**
- [ ] Chrome - ✅ Works
- [ ] Firefox - ✅ Works
- [ ] Edge - ✅ Works
- [ ] Safari - ✅ Works (if on Mac)

**Responsive Design:**
- [ ] Desktop view (1920x1080) - ✅ Works
- [ ] Tablet view (768px) - ✅ Works
- [ ] Mobile view (375px) - ✅ Works

---

## 🎯 Final Sign-Off

**All tests passed?** ✅ You're ready to teach!

**If any test failed:**
1. Review the error message carefully
2. Check the troubleshooting section above
3. Review the specific component (models, views, templates, etc.)
4. Ask for help if stuck (reference README.md or GETTING_STARTED.md)

---

## ⏰ Pre-Class Timing

**Recommended timeline:**
- 30 min before class: Check server starts
- 15 min before class: Load sample data
- 5 min before class: Open browser and have URLs ready
- During class: Reference this checklist as needed

---

## 💾 Backup Important Files

Before teaching (optional but recommended):

```bash
# Copy entire project
copy c:\path\to\python_crud\ c:\path\to\python_crud_backup\

# Or copy just database
copy db.sqlite3 db.sqlite3.backup
```

---

**You're all set! Good luck with your class! 🎓**

For issues, check:
1. This checklist
2. `GETTING_STARTED.md`
3. `README.md`
4. `TEACHING_PLAN.md`
