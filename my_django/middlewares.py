#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from django.utils.deprecation import MiddlewareMixin


class Mypublisher(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method == 'OPTIONS':
            # 证明是复杂的请求
            response['Access-Control-Allow-Methods'] = 'DELETE'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
