#!/usr/bin/python
# -*- coding: utf-8 -*-

from bson import json_util
import json

def handle_encode(self, items, is_multiple):
    if (is_multiple):
        return [json.loads(json.dumps(item, indent=4, default=json_util.default)) for item in items]
    return [json.loads(json.dumps(items, indent=4, default=json_util.default))]