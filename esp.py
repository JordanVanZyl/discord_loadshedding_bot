import requests
from dateutil import parser
import json
import credentials



def parse_response(res) -> str:
    schedule_string = ''
    res = json.loads(res.text)

    for event in res['events']:
        start = parser.parse(event['start'], ignoretz=True)
        end = parser.parse(event['end'], ignoretz=True)
        schedule_string += event['note']+'\n'\
                            +f'\tStart: {start}\n'\
                            +f'\tEnd: {end}\n'

    return schedule_string

def get_next_schedules() -> str:
    area_id = 'jhbcitypower2-16-cresta'
    url = f'https://developer.sepush.co.za/business/2.0/area?id={area_id}'
    headers = {'token':f'{credentials.get_esp_api_key()}'}
    payload = {}

    res = requests.request('GET', url=url, headers=headers, data=payload)
    parsed_response = parse_response(res)

    return parsed_response

def search_areas(keyword) -> str:
    url = f'https://developer.sepush.co.za/business/2.0/areas_search?text={keyword}'
    headers = {'token':f'{credentials.get_esp_api_key()}'}
    payload = {}
    res = requests.request('GET', url=url, headers=headers, data=payload)
    res = json.loads(res)
    #TODO Parse json object and convert into a string
    return res
