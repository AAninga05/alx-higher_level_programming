#!/usr/bin/python3
""" Includes a `from_json_string` model"""
import json


def from_json_string(my_str):
    '''
        Converting string into object
    '''
    return (json.loads(my_str))
