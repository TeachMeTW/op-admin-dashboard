import json
import os

import requests

from utils.constants import valid_trip_columns, valid_uuids_columns


STUDY_NAME = os.getenv('STUDY_NAME')
PATH = os.getenv('CONFIG_PATH')
CONFIG_URL = PATH + STUDY_NAME + ".nrel-op.json"
response = requests.get(CONFIG_URL)
permissions = json.loads(response.text).get("admin_dashboard", {})


def has_permission(perm):
    return True if permissions.get(perm) is True else False


def get_trips_columns():
    columns = set(valid_trip_columns)
    for column in permissions.get("data_trips_columns_exclude", []):
        columns.discard(column)
    return columns


def get_uuids_columns():
    columns = set(valid_uuids_columns)
    for column in permissions.get("data_uuids_columns_exclude", []):
        columns.discard(column)
    return columns


def get_token_prefix():
    return permissions['token_prefix'] + '_' if permissions.get('token_prefix') else ''
