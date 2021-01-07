#extratags.py
import os
from django import template

register = template.Library()

@register.filter
def getf(value):
  return os.path.basename(value)

@register.filter
def verbose_name(obj):
  return obj._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
  return obj._meta.verbose_name_plural


@register.simple_tag
def get_verbose_field_name(instance, field_name):
#    print( dir(instance._meta.get_field(field_name).verbose_name))
#    print( vars(instance._meta.get_field(field_name).verbose_name))
#    print(      instance._meta.get_field(field_name).verbose_name.title())
    return instance._meta.get_field(field_name).verbose_name.title()


#@register.simple_tag
#def get_verbose_field_name(obj, field_name):
#  return obj._meta.get_field(field_name).verbose_name.title()


#@register.simple_tag
#def get_verbose_field_name(instance, field_name):
#  myinstance = eval(instance.split('.')[1].title())
#  return myinstance._meta.get_field(field_name).verbose_name.title()


@register.filter
def filename(value):
    return os.path.basename(value)
