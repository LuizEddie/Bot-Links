import urllib.request
import os
import json
from datetime import date
import time

try:
    file_path = ""
    data = []

    def get_links_status(url):
        try:
            urllib.request.urlopen(url['url'])
            print(url['name'] + ": " + "Online")
            data.append(url['name'] + ": Online")
        except Exception as e:
            print(url['name'] + ": " + "Offline")
            data.append(url['name'] + ": Offline")
            print("  Erro: " + str(e))


    def read_data_json():
        caminhojson = "Links.json"
        with open(caminhojson, "r") as json_data:
            data = json.load(json_data)

        print("Dados Carregados")
        links = data['links']

        for link in links:
            get_links_status(link)

        write_log_file()

    def create_log_file():
        global file_path
        file_path = str(date.today()) + " " + str(time.time()) + ".txt"
        open("log/" + file_path, "x")

        read_data_json()

    def write_log_file():
        file = open("log/" + file_path, "w")
        file.write(str(date.today()) + " " + str(time.time()) + "\n\n")
        for d in data:
            file.write(str(d) + "\n")

        file.close()

    create_log_file()

    os.system("pause")

except Exception as error:
    print(error)
    os.system("pause")