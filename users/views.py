from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()

        if not user:
            messages.error(request, "No account found with this email")
            return redirect("forgot_password")

        # Send dummy reset link (you will upgrade later with token)
        send_mail(
            "Reset your Digital Gold account password",
            "Click here to reset your password: http://127.0.0.1:8000/reset-confirm/",
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )
        messages.success(request, "Reset link has been sent to your email ✅")
        return redirect("forgot_password")

    return render(request, "forgot_password.html")

def reset_confirm(request):
    if request.method == "POST":
        p1 = request.POST.get("password1")
        p2 = request.POST.get("password2")

        if p1 != p2:
            messages.error(request, "Passwords do not match.")
            return redirect("reset_confirm")

        # Example: get the first user (in real setup use token)
        user = User.objects.first()
        user.set_password(p1)
        user.save()
        messages.success(request, "Password updated successfully! Please login.")
        return redirect("login")

    return render(request, "reset_confirm.html")
