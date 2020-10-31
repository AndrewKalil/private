#!/usr/bin/python3
from datadog import initialize, api

options = {
    'api_key': '29e82f9fd53870f2073d32eea90279a6',
    'app_key': 'd0e2a43dab0d90278881c800ca842a63bcd3a1ef'
}

initialize(**options)

print(api.Dashboard.get_all())