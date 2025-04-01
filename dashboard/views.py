from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Home View
def home(request):
    return render(request,'dashboard/home.html')

@login_required
def dashboard(request):
    projects = Project.objects.filter(user=request.user)  # Show only user’s projects
    return render(request, 'dashboard/dashboard.html', {'projects': projects})
    

# Create Project
@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)  # Don't save yet
            project.user = request.user        # Assign the logged-in user
            project.save()                     # Now save
            return redirect('dashboard')            # Redirect to home after creation
    else:
        form = ProjectForm()
    return render(request, 'dashboard/project_form.html', {'form': form})

# Update Project
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/project_form.html', {'form': form})

# Delete Project
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/project_confirm_delete.html', {'project': project})

#################################### TASK ############################################


# Task List (Inside Project Detail Page)
@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = project.tasks.all()  # Fetch tasks related to this project
    return render(request, 'dashboard/project_detail.html', {'project': project, 'tasks': tasks})

# Create Task
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'dashboard/task_form.html', {'form': form, 'project': project})

# Update Task
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=task.project.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'dashboard/task_form.html', {'form': form, 'project': task.project})

# Delete Task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    project_id = task.project.id
    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', project_id=project_id)
    return render(request, 'dashboard/task_confirm_delete.html', {'task': task})


############################## USer ##############################


# User Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/signup.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})

# User Logout
def logout_view(request):
    logout(request)
    return redirect('home')