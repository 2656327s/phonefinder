#from app.models import PhoneModel
# filter all phones to fit specifications
import os
import path
import json


def filterPhones(specs):
    # example specs, {"name":"","brand":"","earliest_release":2000,"latest_release":3000,"min_storage":1,"max_storage":100,"resolution":"","min_ram":1,"max_ram":4"}
    # if the value is blank, then it should be treated as all phones passing the test

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file_path = os.path.join(BASE_DIR, 'phones.json')
    with open(json_file_path) as json_file:
        phones = json.load(json_file)
        json_file.close()

    filtered_phones = []
    for phone in phones:
        if specs["brand"] != "" and phone["brand"] != specs["brand"]:
            continue
        if int(float(phone["releaseYear"])) < int(specs["min_year"]) or int(float(phone["releaseYear"])) > int(specs["max_year"]):
            continue
        if int(float(phone["storage"])) < int(float(specs["min_storage"])) or int(float(phone["storage"])) > int(float(specs["max_storage"])):
            continue
        if int(phone["resolution"].split("x")[0]) < int(specs["min_width"]) or int(phone["resolution"].split("x")[0]) > int(specs["max_width"]):
            continue
        if int(phone["resolution"].split("x")[1]) < int(specs["min_height"]) or int(phone["resolution"].split("x")[1]) > int(specs["max_height"]):
            continue
        if int(float(phone["ram"])) < int(float(specs["min_ram"])) or int(float(phone["ram"])) > int(float(specs["max_ram"])):
            continue

        filtered_phones.append(phone)
    # now theyve been filtered, the only remaining elements are the ones that fit the specs
    return filtered_phones
