"""
    @author - Waruna Nissanka
    @email - warunanissanka44@gmail.com
    @web - www.waruna.me
    @project - UnivoX

    Description - Extractor.
"""

from app import app, db
from flask import jsonify
from models.NVQStudent import NVQStudent
from models.ALStudent import ALStudent
from exceptions.validations import ValidationError
import re

MAXUMUM_ROWS = 500

# extract records
def extract_nvq_details(records):
    result = []

    if len(records) > MAXUMUM_ROWS:
        raise ValidationError(str.format('Maximum row count is 500'))
        
    if (len(records) > 1):
        for record in records[1:]:
            check_nvq_student_already_exists(record[1].upper())

            # details = {
            #     'application_no': validate_nvq_application_number(record[1].upper()),
            #     'identity_no': validate_identity_number(record[2]),
            #     'index_no': check_empty_column('Index number is required', record[1], record[3]),
            #     'initials': check_empty_column('Initial letters are required', record[1], record[4]),
            #     'surename': check_empty_column('Surename is required', record[1], record[5]),
            #     'title': check_empty_column('Title is required', record[1], record[6]),
            #     'gender': check_empty_column('Initial letters required', record[1], record[7]),
            #     'ethnicity': check_empty_column('Ethnicity is required', record[1], record[8]),
            #     'address_1': check_empty_column('Address line one is required', record[1], record[9]),
            #     'address_2': check_empty_column('Address line two is required', record[1], record[10]),
            #     'city': check_empty_column('City is required', record[1], record[11]),
            #     'district': check_empty_column('District is required', record[1], record[12]),
            #     'telephone': record[13],
            #     'mobile': check_empty_column('Mobile is required', record[1], record[14]),
            #     'email': record[15],
            #     'diploma': check_empty_column('Diploma is required', record[1], record[16]),
            #     'preference_1': check_empty_column('Preference one is required', record[1], record[17]),
            #     'preference_2': record[18],
            #     'preference_3': record[19],
            #     'remarks': record[20],
            #     'permenent_address': record[21]
            # }

            details = {
                'application_no': validate_nvq_application_number(record[1].upper()),
                'identity_no': validate_identity_number(record[2]),
                'index_no': record[3],
                'initials': record[4],
                'surename': record[5],
                'title': record[6],
                'gender': record[7],
                'ethnicity': record[8],
                'address_1': record[9],
                'address_2': record[10],
                'city': record[11],
                'district': record[12],
                'telephone': record[13],
                'mobile': record[14],
                'email': record[15],
                'diploma': record[16],
                'preference_1': record[17],
                'preference_2': record[18],
                'preference_3': record[19],
                'remarks': record[20],
                'permenent_address': record[21],
                'permanent_district': record[22]
            }
            result.append(details)
    return result

# extract records
def extract_al_details(records):
    result = []

    if len(records) > MAXUMUM_ROWS:
        raise ValidationError(str.format('Maximum row count is 500'))
        
    if (len(records) > 1):
        for record in records[1:]:
            check_al_student_already_exists(record[1].upper())

            # details = {
            #     'application_no': validate_al_application_number(record[1].upper()),
            #     'identity_no': validate_identity_number(record[2]),
            #     'initials': check_empty_column('Initial letters are required', record[1], record[3]),
            #     'surename': check_empty_column('Surename is required', record[1], record[4]),
            #     'title': check_empty_column('Title is required', record[1], record[5]),
            #     'gender': check_empty_column('Initial letters required', record[1], record[6]),
            #     'ethnicity': check_empty_column('Ethnicity is required', record[1], record[7]),
            #     'address_1': check_empty_column('Address line one is required', record[1], record[8]),
            #     'address_2': check_empty_column('Address line two is required', record[1], record[9]),
            #     'city': check_empty_column('City is required', record[1], record[10]),
            #     'district': check_empty_column('District is required', record[1], record[11]),
            #     'telephone': record[12],
            #     'mobile': check_empty_column('Mobile is required', record[1], record[13]),
            #     'email': record[14],
            #     'preference_1': check_empty_column('Preference one is required', record[1], record[18]),
            #     'preference_2': record[19],
            #     'preference_3': record[20],
            #     'stream': check_empty_column('Diploma is required', record[1], record[15]),
            #     'al_index_no': check_empty_column('Diploma is required', record[1], record[16]),
            #     'z_score': check_empty_column('Diploma is required', record[1], record[17]),
            #     'al_ict_grade': record[21],
            #     'comm_media_grade': record[22],
            #     'gen_eng_grade': record[23],
            #     'com_gen_test_grade': record[24]
            # }

            details = {
                'application_no': validate_al_application_number(record[1].upper()),
                'identity_no': validate_identity_number(record[2]),
                'initials': record[3],
                'surename': record[4],
                'title': record[5],
                'gender': record[6],
                'ethnicity': record[7],
                'address_1': record[8],
                'address_2': record[9],
                'city': record[10],
                'district': record[11],
                'telephone': record[12],
                'mobile': record[13],
                'email': record[14],
                'preference_1': record[18],
                'preference_2': record[19],
                'preference_3': record[20],
                'stream': record[15],
                'al_index_no': record[16],
                'z_score': record[17],
                'al_ict_grade': record[21],
                'comm_media_grade': record[22],
                'gen_eng_grade': record[23],
                'com_gen_test_grade': record[24],
                'permanent_district': record[22]
            }
            result.append(details)
    return result


def check_nvq_student_already_exists(application_number):
    applicant = NVQStudent.query.filter_by(application_no=application_number.upper()).first()
    if applicant:
        raise ValidationError(str.format('Applicant already exists - {}', applicant.application_no))
    pass

def check_al_student_already_exists(application_number):
    applicant = ALStudent.query.filter_by(application_no=application_number.upper()).first()
    if applicant:
        raise ValidationError(str.format('Applicant already exists - {}', applicant.application_no))
    pass

def validate_nvq_application_number(number):
    if re.search("^NVQ/\w+/B[1|2]{1}/\d+$", number):
        return str(number)
    else:
        raise ValidationError(str.format('Invalid application number - {}', number))

def validate_al_application_number(number):
    if re.search("^AL/\w+/\d+/\d+$", number):
        return str(number)
    else:
        raise ValidationError(str.format('Invalid application number - {}', number))

def validate_identity_number(number):
    if re.search("^(?:19|20)?\d{2}(?:[01235678]\d\d(?<!(?:000|500|36[7-9]|3[7-9]\d|86[7-9]|8[7-9]\d)))\d{4}(?:[vVxX0-9])$", number):
        return str(number)
    else:
        raise ValidationError(str.format('Invalid identity number - {}', number))

def validate_only_strings(value):
    if re.search("^[a-zA-Z]+", value):
        return str(value)
    else:
        raise ValidationError(str.format('Invalid input value - {}', value))

def check_empty_column(message, application_no, value):
    if not value:
        raise ValidationError(str.format('{} - {}', message, application_no))
    else:
        return value