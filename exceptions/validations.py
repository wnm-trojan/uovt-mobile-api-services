"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Exceptions.
"""

class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
