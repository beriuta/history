from rest_framework import permissions


class MyPermission(permissions.BasePermission):
    message = '此项目只限vip用户,请充值vip'

    def has_permission(self, request, view):
        if request.user.type in [1,3]:
            return True
        return False
