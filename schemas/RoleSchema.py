"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Role schema.
"""

from app import ma

class RoleSchema(ma.Schema):
  class Meta:
    fields = ('role_code', 'role_name')