# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports

# Core Django imports
from django import template
# Third-party app imports

# Realative imports of the 'app-name' package


register = template.Library()


@register.filter('has_group')
def has_group(user, group_name):
    from django.contrib.auth.models import User
    """
    Verifica se este usuário pertence a un grupo en la empresa actual
    """

    user = User.objects.get(username = user)
    rol = user.groups.all().values_list('name', flat=True)
    groups = user.groups.filter(name__in = rol).values_list('name', flat=True)
    return True if group_name in groups else False

@register.filter('get_rol')
def get_rol(user):
    from django.contrib.auth.models import User
    """
    Verifica el nombre del rol que tiene el usuario
    """

    user = User.objects.get(username = user)
    print(user.groups.all().first())
    rol = user.groups.get(name = user.groups.all().first())
    return rol
