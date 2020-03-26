#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials


scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'aaylc-c1cead84ee51.json', scope)

client = gspread.authorize(creds)

sheet = client.open('InternWorkPlan-FaizulHadiman').sheet1


pp = pprint.PrettyPrinter()


# aaylc = sheet.get_all_values()
aaylc = sheet.cell(41, 8).value


pp.pprint(aaylc)
