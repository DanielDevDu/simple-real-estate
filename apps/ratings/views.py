"""
-------------------------
Views to Profiles models
-------------------------
"""
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# My models and serializers
from apps.profiles.models import Profile

from .models import Rating

User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    """
    ----------------------------
    Create a review for an agent
    ----------------------------
    """
    agent_profile = Profile.objects.get(id=profile_id)
    data = request.data

    profile_user = User.objects.get(pkid=agent_profile.user.pkid)
    if profile_user.email == request.user.email:
        format_response = {"message": "You cannot review yourself"}
        return Response(format_response, status=status.HTTP_403_FORBIDDEN)

    alreadyExists = agent_profile.agent_review.filter(
        agent__pkid=profile_user.pkid
    ).exists()

    if alreadyExists:
        format_response = {"detail": "Profile already reviewed"}
        return Response(format_response, status=status.HTTP_400_BAD_REQUEST)
    elif data["rating"] == 0:
        format_response = {"detail": "Please select a rating"}
        return Response(format_response, status=status.HTTP_400_BAD_REQUEST)
    else:
        review = Rating.objects.create(
            rater=request.user,
            agent=agent_profile,
            rating=data["rating"],
            comment=data["comment"],
        )
        reviews = agent_profile.agent_review.all()
        agent_profile.num_reviews = len(reviews)

        total = 0
        for review in reviews:
            total += review.rating

        return Response("Review Added", status=status.HTTP_200_OK)
