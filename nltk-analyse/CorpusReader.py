__author__ = 'Colin Sippl, Florian Fuchs'
# -*- coding: utf-8 -*-
# lese Songtext-Korpusdatei
from bs4 import BeautifulSoup
import nltk
import re


class CorpusReader(object):
    def __init__(self, file_name, corpus_path):
        self.file_name = file_name
        self.corpus_path = corpus_path
        print("...Pfad der einzulesenden Korpusdatei: \"" + corpus_path + "\"...")
        print("...Starte Einlesen der Korpusdateien von \"" + self.file_name + "\"...")

    def selectTextFromIntervall(self, year_start, year_end, author_name):
        if author_name == "":
            self.print_every_date(year_start, year_end)
        else:
            print()

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

    def select_taggedsongs_from_author(self, author_name, date_start, date_end):
        pattern = re.compile(" " + author_name + "  ")
        corpora = list()
        text = ""
        text_remain = ""
        for song in self.soup.findAll('song'):
            date = 0
            if song.find("date", text=True) is not None:
                date = int(song.find("date", text=True).text)
            if (date >= date_start) & (date <= date_end):
                query = ""
                if song.find("author", text=pattern) is not None:
                    query = song.find("author", text=pattern).text
                    #print(query + " " + author_name + " " + str(pattern))
                if author_name in query:
                    text += " " + song.find("text", text=True).text
            else:
                query = ""
                if song.find("author", text=pattern) is not None:
                    query = song.find("author", text=pattern).text
                if author_name in query:
                    text_remain += " " + song.find("text", text=True).text
        text = [nltk.tag.str2tuple(t) for t in text.split()]
        text = [(a.lower(),b) for (a,b) in text]
        text_remain = [nltk.tag.str2tuple(t) for t in text_remain.split()]
        text_remain = [(a.lower(), b) for (a, b) in text_remain]
        corpora.append(text)
        corpora.append(text_remain)
        return corpora

    def return_tagged_tokens(self):
        return [item for sublist in self.pos_file for item in sublist]

