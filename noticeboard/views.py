from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from .models import *

def dashboard(request):
    """ Publicly lists all notices """
    notices = Notice.objects.all().order_by('-id')
    return render(request, 'noticeboard/dashboard.html', {"notices": notices})

@csrf_exempt
def post_notice(request):
    """ Allows admin to add new notices """
    admin_email = request.session.get("admin_email")
    if not admin_email:
        return redirect('admin_login')

    if request.method == "POST":
        title = request.POST.get("title", "No Title")
        description = request.POST.get("description", "No Content")
        category = request.POST.get("category", "General")

        notice = Notice(title=title, description=description, category=category)
        notice.save()
        return redirect('dashboard')
    
    return render(request, 'noticeboard/admin_panel.html')

@csrf_exempt
def delete_notice(request):
    """ Allows admin to delete notices """
    admin_email = request.session.get("admin_email")
    if not admin_email:
        return redirect('admin_login')

    if request.method == "POST":
        notice_id = request.POST.get("notice_id")
        Notice.objects.filter(id=notice_id).delete()
        return JsonResponse({"status": "success", "message": "Notice deleted"})

    return JsonResponse({"status": "failed", "message": "Invalid request"})

@csrf_exempt
def update_notice(request):
    """ Allows admin to update notices """
    admin_email = request.session.get("admin_email")
    if not admin_email:
        return redirect('admin_login')

    if request.method == "POST":
        notice_id = request.POST.get("notice_id")
        new_title = request.POST.get("title")
        new_description = request.POST.get("description")
        new_category = request.POST.get("category")

        notice = Notice.objects.filter(id=notice_id).first()
        if notice:
            notice.title = new_title
            notice.description = new_description
            notice.category = new_category
            notice.save()
            return JsonResponse({"status": "success", "message": "Notice updated"})
    
    return JsonResponse({"status": "failed", "message": "Invalid request"})

def admin_login(request):
    """ Admin login page """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        print(f"Login attempt: {email} | {password}")  # Debugging

        admin = AdminUser.objects.filter(email=email, password=password).first()
        if admin:
            request.session["admin_email"] = email
            print("Login successful!")  # Debugging
            return redirect('admin_panel')  # Ensure this URL is correct
        else:
            print("Login failed!")  # Debugging
            return render(request, 'noticeboard/admin_login.html', {"error": "Invalid credentials"})

    return render(request, 'noticeboard/admin_login.html')


def admin_panel(request):
    """ Admin dashboard to manage notices """
    admin_email = request.session.get("admin_email")
    if not admin_email:
        return redirect('admin_login')

    notices = Notice.objects.all()
    return render(request, 'noticeboard/admin_panel.html', {"notices": notices})