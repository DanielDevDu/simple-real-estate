from django.core.mail import send_mail
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from real_estate.settings.development import DEFAULT_FROM_EMAIL

from .models import Enquiry


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def send_enquiry_email(request):
    """
    ----------------------------
    Send an enquiry email to an agent
    ----------------------------
    """
    data = request.data
    try:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)
        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response(
            {"success" ": Your Enquiry was succesfully submitted"},
            status=status.HTTP_200_OK,
        )
    except Exception as err:
        # raise err
        return Response(
            {"fail": "Your Enquiry was not submitted"},
            status=status.HTTP_400_BAD_REQUEST,
        )
