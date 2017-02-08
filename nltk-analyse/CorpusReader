__author__ = 'Colin Sippl'
# -*- coding: utf-8 -*-
# lese Songtext-Korpusdatei
from bs4 import BeautifulSoup

#Name der Korpusdatei
file_name = "Corpus_Dylan452.xml"
#Pfad der Korpusdatei
corpus_path = './corpus/'

def main():
    reader = CorpusReader(file_name, corpus_path)
    reader.read_file()
    reader.parse_file()
    reader.print_every_song()
    reader.print_every_title()
    reader.print_every_date(1960, 1970)

class CorpusReader(object):
    def __init__(self, file_name, corpus_path):
        self.file_name = file_name
        self.corpus_path = corpus_path
        print("...Pfad der einzulesenden Korpusdatei: \"" + corpus_path + "\"...")
        print("...Starte Einlesen der Korpusdateien von \"" + self.file_name + "\"...")

    def read_file(self):
        self.xml_file = open(self.corpus_path + self.file_name, encoding="utf8")

    def parse_file(self):
        self.soup = BeautifulSoup(self.xml_file, 'xml')

    def print_every_date(self, start, end):
        for text_element in self.soup.findAll('date', text=True):
            #print(text_element)
            text_element = int(text_element.text)
            if (text_element >= start) & (text_element <= end):
                print(text_element)

    def print_every_song(self):
        for text_element in self.soup.findAll('text', text=True):
            print(text_element.text)

    def print_every_title(self):
        for title_element in self.soup.findAll('title', text=True):
            print(title_element.text)


if __name__ == '__main__':
    print('This program is being run by itself')
    main()
else:
    print('I am being imported from another module')