"""
-------------------------
Views to Profiles models
-------------------------
"""
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile, ProfileNotFound

# My models and serializers
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UpdateProfileSerializer


class AgentListAPIView(generics.ListAPIView):
    """
    -------------------------
    List all agents
    -------------------------
    """

    queryset = Profile.objects.filter(is_agent=True)
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = (ProfileJSONRenderer,)


class TopAgentListAPIView(generics.ListAPIView):
    """
    -------------------------
    List all top agents.
    -------------------------
    """

    queryset = Profile.objects.filter(top_agent=True)
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # renderer_classes = (ProfileJSONRenderer,)


class GetProfileAPIView(APIView):
    """
    -------------------------
    Get profile by id.
    -------------------------
    """

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)

    def get(self, request):
        """
        -------------------------
        Get profile by id.
        -------------------------
        """
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProfileView(APIView):
    """
    -------------------------
    Update profile by id.
    -------------------------
    """

    permission_classes = (permissions.IsAuthenticated,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        """
        ---------------------------
        Update profile by username
        ---------------------------
        """
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user.profile, data=data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
