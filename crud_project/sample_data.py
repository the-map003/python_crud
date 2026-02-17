"""
Sample data script to populate the database with test students.
Run with: python manage.py shell < sample_data.py
Or manually in Django shell: python manage.py shell
Then: exec(open('sample_data.py').read())
"""

from datetime import datetime, timedelta
from crud_app.models import Student

# Clear existing students (optional)
# Student.objects.all().delete()

# Sample student data
students_data = [
    {
        'first_name': 'Rajesh',
        'last_name': 'Kumar',
        'email': 'rajesh.kumar@example.com',
        'roll_number': 'CSE001',
        'phone': '9876543210',
        'date_of_birth': '2004-05-15',
        'address': '123 Main Street, Delhi, India'
    },
    {
        'first_name': 'Priya',
        'last_name': 'Singh',
        'email': 'priya.singh@example.com',
        'roll_number': 'CSE002',
        'phone': '9876543211',
        'date_of_birth': '2004-08-22',
        'address': '456 Park Avenue, Mumbai, India'
    },
    {
        'first_name': 'Arjun',
        'last_name': 'Patel',
        'email': 'arjun.patel@example.com',
        'roll_number': 'CSE003',
        'phone': '9876543212',
        'date_of_birth': '2005-01-10',
        'address': '789 Oak Road, Bangalore, India'
    },
    {
        'first_name': 'Neha',
        'last_name': 'Sharma',
        'email': 'neha.sharma@example.com',
        'roll_number': 'CSE004',
        'phone': '9876543213',
        'date_of_birth': '2004-11-30',
        'address': '321 Elm Street, Chennai, India'
    },
    {
        'first_name': 'Vikram',
        'last_name': 'Reddy',
        'email': 'vikram.reddy@example.com',
        'roll_number': 'CSE005',
        'phone': '9876543214',
        'date_of_birth': '2005-03-18',
        'address': '654 Maple Drive, Hyderabad, India'
    },
    {
        'first_name': 'Anjali',
        'last_name': 'Verma',
        'email': 'anjali.verma@example.com',
        'roll_number': 'CSE006',
        'phone': '9876543215',
        'date_of_birth': '2004-07-25',
        'address': '987 Birch Lane, Pune, India'
    },
    {
        'first_name': 'Karan',
        'last_name': 'Nair',
        'email': 'karan.nair@example.com',
        'roll_number': 'CSE007',
        'phone': '9876543216',
        'date_of_birth': '2005-02-14',
        'address': '147 Cedar Street, Kolkata, India'
    },
    {
        'first_name': 'Divya',
        'last_name': 'Gupta',
        'email': 'divya.gupta@example.com',
        'roll_number': 'CSE008',
        'phone': '9876543217',
        'date_of_birth': '2004-09-05',
        'address': '258 Spruce Avenue, Ahmedabad, India'
    },
]

# Create students
created_count = 0
skipped_count = 0

for student_data in students_data:
    # Check if student already exists
    if Student.objects.filter(email=student_data['email']).exists():
        print(f"⏭️ Skipped: {student_data['first_name']} {student_data['last_name']} (already exists)")
        skipped_count += 1
    else:
        try:
            student = Student.objects.create(**student_data)
            print(f"✅ Created: {student.first_name} {student.last_name} ({student.roll_number})")
            created_count += 1
        except Exception as e:
            print(f"❌ Error creating {student_data['first_name']}: {str(e)}")

print(f"\n📊 Summary: {created_count} created, {skipped_count} skipped")
print(f"📈 Total students in database: {Student.objects.count()}")
