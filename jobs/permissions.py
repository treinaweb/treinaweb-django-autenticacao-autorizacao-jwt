from rest_framework.permissions import BasePermission


class JobApplicantsPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (request.method == "GET" and request.user and request.user.is_staff)
            or (
                request.method == "POST"
                and request.user
                and request.user.is_authenticated
                and not request.user.is_staff
            )
        )
