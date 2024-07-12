#!/usr/bin/env python3
"""Authenticating module for the API.
"""
import re
from flask import abort, request
from typing import List, TypeVar
from models.user import User


class Auth:
    """Authentication class.
    """
   
    def require_auth(
        self, path: str, excluded_paths: List[str]
    ) -> bool:
        """ determines if authentication is required """
        if path is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path = path + '/'
        for pth in excluded_paths:
            if pth[-1] == '*':
                pth = pth[:-1] + '.*'
            if re.fullmatch(pth, path):
                return False

        return True

   def authorization_header(self, request=None) -> str:
        """ doc str """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header:
            return auth_header
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user from the request.
        """
        return None
