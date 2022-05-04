import sys
import json
import csv 

import requests


def get_geolocation_JSON(ipv4):
    response = requests.get(f'https://geolocation-db.com/json/{ipv4}&position=true')
    response_json = response.json()
    return response_json

log_path = sys.argv[1]

with open('ip-location.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['IP', 'Location', 'Timestamp'])
    with open(log_path,'r',encoding = 'utf-8') as log_file:
        line_list = log_file.readlines()
        print('Started locating the IPs from the log file...')
        number_of_lines = len(line_list)
        for i, line in enumerate(line_list):
            print(f'Locating... {i}/{number_of_lines}')
            split_line = line.split(' - - ')
            ipv4 = split_line[0]
            split_line = split_line[1].split('] ')
            timestamp = split_line[0][1:]
            location_json = get_geolocation_JSON(ipv4)
            location = location_json['country_name']
            writer.writerow([ipv4, location, timestamp])
        print('Done!')