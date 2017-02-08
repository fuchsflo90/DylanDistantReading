__author__ = 'Colin Sippl'
# -*- coding: utf-8 -*-
# lese Songtext-Korpusdatei
from bs4 import BeautifulSoup
from CorpusText import CorpusText
from CSVwriter import CSVwriter
import nltk
import re

#Name der Korpusdatei
file_name = "Corpus_Dylan452.xml"
#Pfad der Korpusdatei
corpus_path = './corpus/'

def main():
    reader = CorpusReader(file_name, corpus_path)
    reader.read_file()
    reader.parse_file()
    #reader.print_every_song()
    #reader.print_every_title()
    #reader.print_every_date(1960, 1970)

    untersuchungsbereich = reader.select_songs_from_author("Bob Dylan", 1960, 1970)
    untersuchungsbereich = re.sub('[.?!,„":;`€$\'()#|0-9]', '', untersuchungsbereich)
    untersuchungsbereich = nltk.word_tokenize(untersuchungsbereich)
    print(untersuchungsbereich)
    kontrollbereich = reader.select_songs_from_author("Bob Dylan", 1971, 2020)
    kontrollbereich = re.sub('[.?!,„":;`€$\'()#|0-9]', '', kontrollbereich)
    kontrollbereich = nltk.word_tokenize(kontrollbereich)

    # Berechne Anzahl der Tokens pro Korpus-Text
    length_a = CorpusText.count_tokens(untersuchungsbereich)
    length_b = CorpusText.count_tokens(kontrollbereich)

    print(length_a)
    print(length_b)

    # *****Stoppwortliste: JA
    fredDist_a = CorpusText.word_rank_absolut_freq(True, "dylan_int", untersuchungsbereich, 'all_words')
    fredDist_b = CorpusText.word_rank_absolut_freq(True, "dylan_rest", kontrollbereich, 'all_words')

    difvals = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
    CSVwriter.write_text_differences("significant_text_differences", "dylan_int", True, 300, "words", difvals, 'all_words')
    # vice versa
    difvals = CorpusText.calculate_significant_word_differences(fredDist_b, fredDist_a,
                                                         length_a, length_b)
    CSVwriter.write_text_differences("significant_text_differences", "dylan_rest", True, 300, "words", difvals, 'all_words')

    # *****Stoppwortliste: JA
    difvals = CorpusText.calculate_significant_bigram_differences(True, untersuchungsbereich, kontrollbereich)
    CSVwriter.write_text_differences("significant_text_differences", "dylan_int", True, 300, "words", difvals, 'bigrams')
    difvals = CorpusText.calculate_significant_bigram_differences(True, kontrollbereich, untersuchungsbereich)
    CSVwriter.write_text_differences("significant_text_differences", "dylan_rest", True, 300, "words", difvals, 'bigrams')

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

    def select_songs_from_author(self, author_name, date_start, date_end):
        pattern = re.compile(" " + author_name + "  ")
        text = ""
        for song in self.soup.findAll('song'):
            date = 0
            if song.find("date", text=True) is not None:
                date = int(song.find("date", text=True).text)
            if (date >= date_start) & (date <= date_end):
                #print("++++++++++++++++++++++++++++++++++++++++++++ " + str(date))
                query = ""
                if song.find("author", text=pattern) is not None:
                    query = song.find("author", text=pattern).text
                if author_name in query:
                    text += " " + song.find("text", text=True).text
        return text


if __name__ == '__main__':
    print('This program is being run by itself')
    main()
else:
    print('I am being imported from another module')