#!/usr/bin/python
# -*- coding: utf-8 -*-

from bson import json_util
import json

def handle_encode(self, items):
    # Only one item
    if type(items) is dict:             
        return [json.loads(json.dumps(items, indent=4, default=json_util.default))]
    # Multiple items
    return [json.loads(json.dumps(item, indent=4, default=json_util.default)) for item in items]
