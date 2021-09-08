from rest_framework import permissions

from portal.models import Poll, PollOption


class OwnerPermission(permissions.BasePermission):
    """Permission that checks authentication and only permits owner to update/destroy objects"""

    def has_object_permission(self, request, view, obj):
        # only creator can edit
        if view.action in ["partial_update", "update", "destroy"]:
            if type(obj) == PollOption:
                return request.user == obj.poll.user or request.user.is_superuser
            return request.user == obj.user or request.user.is_superuser
        return True

    def has_permission(self, request, view):
        # ensures that only author of Poll can create its Poll Options
        if view.action == "create" and request.get_full_path() == "/portal/options/":
            try:
                poll = Poll.objects.get(id=request.data["poll"])
                return (
                    request.user.is_authenticated and poll.user == request.user
                ) or request.user.is_superuser
            except KeyError:
                # sometimes sends list then immediate create when
                # rendering DRF HTML, so catching this for testing
                pass
        return request.user.is_authenticated


class TimeSeriesPermission(permissions.BasePermission):
    """Permission that checks for Time Series access (only creator of Poll and admins)"""

    def has_permission(self, request, view):
        poll = Poll.objects.filter(id=view.kwargs["id"])
        # checks if poll exists
        if poll.exists():
            # only poll creator and admin can access
            return (
                poll.first().user == request.user and request.user.is_authenticated
            ) or request.user.is_superuser
        return False
