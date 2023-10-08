from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from django.db.models.functions import Trunc
from django.utils import timezone
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SubletSerializer

from sublet.models import Sublet, SubletImage, Offer, Favorite, Amenity

from sublet.permissions import SubletOwnerPermission, IsSuperUser
from sublet.serializers import SubletSerializer

User = get_user_model()


class Properties(viewsets.ModelViewSet):
    """
    browse:
    Returns a list of Sublets that match query parameters (e.g., amenities) and belong to the user.
    
    create:
    Create a Sublet.
    
    partial_update:
    Update certain fields in the Sublet. Only the owner can edit it.
    
    destroy:
    Delete a Sublet.
    """

    #how to use the sublet owner permission
    permission_classes = [SubletOwnerPermission | IsSuperUser]
    serializer_class = SubletSerializer

    def get_queryset(self):
        # All Sublets for superusers
        if self.request.user.is_superuser:
            return Sublet.objects.all()
        
        # All Sublets where expires_at hasn't passed yet for regular users
        return Sublet.objects.filter(expires_at__gte=timezone.now())

    @action(detail=False, methods=["get"])
    def browse(self, request):
        """Returns a list of Sublets that match query parameters and user ownership."""
        # Get query parameters from request (e.g., amenities, user_owned)
        amenities = request.query_params.getlist("amenities")
        subletter = request.query_params.get("subletter", False)  # Defaults to False if not specified
        
        queryset = Sublet.objects.all()
    
        # Apply filters based on query parameters
        if amenities:
            queryset = queryset.filter(amenities__name__in=amenities)
        if subletter.lower() == "true":
            queryset = queryset.filter(subletter=request.user)
        
        # Serialize and return the queryset
        serializer = SubletSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def view_property(self, request, pk=None):
        """Returns details of a specific Sublet."""
        sublet = self.get_object()
        serializer = SubletSerializer(sublet)
        return Response(serializer.data)
