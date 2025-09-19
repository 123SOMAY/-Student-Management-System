from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Todo, Student

# Create your views here.

# Todo views
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'core/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('todo_list')

def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list')

# Authentication views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        print(f"DEBUG: Attempting login with username='{username}', password='{password}'")
        user = authenticate(request, username=username, password=password)
        print(f"DEBUG: Authentication result: {user}")
        if user is not None:
            login(request, user)
            print(f"DEBUG: Login successful, redirecting to student_list")
            return redirect('student_list')
        else:
            print(f"DEBUG: Authentication failed")
            messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

# Student Management views
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        grades = request.POST.get('grades')
        
        if name and email and course and grades:
            try:
                Student.objects.create(
                    name=name,
                    email=email,
                    course=course,
                    grades=float(grades),
                    created_by=request.user
                )
                messages.success(request, 'Student added successfully!')
                return redirect('student_list')
            except Exception as e:
                messages.error(request, f'Error adding student: {str(e)}')
    
    return render(request, 'core/student_form.html', {
        'action': 'Add',
        'course_choices': Student.COURSE_CHOICES
    })

@login_required
def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.grades = float(request.POST.get('grades'))
        
        try:
            student.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
        except Exception as e:
            messages.error(request, f'Error updating student: {str(e)}')
    
    return render(request, 'core/student_form.html', {
        'student': student,
        'action': 'Edit',
        'course_choices': Student.COURSE_CHOICES
    })

@login_required
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('student_list')
