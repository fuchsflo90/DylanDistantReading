__author__ = 'Colin Sippl, Florian Fuchs'
# -*- coding: utf-8 -*-

import json
import os

class JSONWriter(object):

    @staticmethod
    def writeJSONData (json_data):
        print("...Schreibe Korpus-Metainformationen als JSON-Datei...")
        if not os.path.exists('./output/data/meta/'):
            os.makedirs('./output/data/meta/')
        with open('./output/data/meta/metainfo' + '.json', mode='w', encoding='utf8') as out_file:
            json.dump(json_data, out_file, indent=4)
            out_file.close()