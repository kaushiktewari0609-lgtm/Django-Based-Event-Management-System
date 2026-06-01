from django.core.mail import send_mail
from django.conf import settings

def send_registration_email(user, event):
    send_mail(
        subject=f"Registration confirmed: {event.title}",
        message=(
            f"Hi {user.get_full_name()},\n\n"
            f"You are registered for '{event.title}' on {event.date} "
            f"at {event.start_time} — {event.venue.name}.\n\n"
            f"Your pass will be issued soon. Check 'My Passes' on the portal.\n\n"
            f"Regards,\nEvents Team"
        ),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True,
    )

def send_pass_active_email(user, event, pass_code):
    send_mail(
        subject=f"Your pass is active: {event.title}",
        message=(
            f"Hi {user.get_full_name()},\n\n"
            f"Your pass for '{event.title}' is now ACTIVE.\n"
            f"Pass Code: {pass_code}\n\n"
            f"Show your QR code at the entry gate.\n\n"
            f"Regards,\nEvents Team"
        ),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True,
    )

def send_cancellation_email(user, event):
    send_mail(
        subject=f"Event cancelled: {event.title}",
        message=(
            f"Hi {user.get_full_name()},\n\n"
            f"We're sorry — '{event.title}' scheduled for {event.date} "
            f"has been cancelled.\n\n"
            f"Regards,\nEvents Team"
        ),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True,
    )