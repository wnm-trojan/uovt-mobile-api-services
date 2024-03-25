"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @project - UnivoX

    Description - Status schema.
"""

from app import ma

class StatusSchema(ma.Schema):
    class Meta:
        fields = ('status_code', 'status_name', 'longitude', 'latitude', 'imei_code', 'status')