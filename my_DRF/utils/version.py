from rest_framework import versioning

class My_version(object):
    def determine_version(self, request, *args, **kwargs):
        version = request.query_params.get('version', 'v1')
        return version
