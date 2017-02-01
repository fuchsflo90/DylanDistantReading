__author__ = 'Colin Sippl'
# -*- coding: utf-8 -*-
# lese POS-Korpusdatei
# http://www.nltk.org/api/nltk.corpus.reader.html
from nltk.corpus.reader import TaggedCorpusReader
from SpeechObject import SpeechObject
import nltk

class FileReader(object):
    def __init__(self, file_name, corpus_path):
        self.file_name = file_name
        self.corpus_path = corpus_path
        print("...Pfad der einzulesenden Korpusdatei: \"" + corpus_path + "\"...")
        print("...Starte Einlesen der Korpusdateien von \"" + self.file_name.upper() + "\"...")
        self.read_pos_file()
        self.read_raw_text_by_line()

    def read_pos_file(self):
        self.pos_file = TaggedCorpusReader(self.corpus_path, fileids=None, encoding='utf8').tagged_sents('POS_' + self.file_name + '.txt')

    def return_pos_file(self):
        return self.pos_file

    def return_tagged_tokens(self):
        return [item for sublist in self.pos_file for item in sublist]

    def read_raw_text_by_line(self):
        self.sent_tokenize_list = SpeechObject()
        with open(self.corpus_path + self.file_name + '.txt', encoding="utf8") as neu_sentence:
            for line in neu_sentence:
                self.sent_tokenize_list.add_quote(line)

    def return_raw_text_lines(self):
        return self.sent_tokenize_list.return_all_quotes()

    def return_raw_text_tokens(self):
        raw_text = open(self.corpus_path + self.file_name + '.txt', encoding="utf8").read()
        return nltk.Text(nltk.word_tokenize(raw_text))

    def return_pos_text_tokens(self):
        return nltk.Text(nltk.word_tokenize(self.pos_file))
