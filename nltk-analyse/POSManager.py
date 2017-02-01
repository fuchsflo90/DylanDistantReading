__author__ = 'Colin Sippl'
# -*- coding: utf-8 -*-

import nltk

class POSManager(object):
    def __init__(self):
        self.pos_files = {}
        self.raw_text_lines_list = {}

    def add_corpus_files(self, key, pos_file, raw_text_lines_list):
        self.pos_files[key] = pos_file
        self.raw_text_lines_list[key] = raw_text_lines_list

    def return_word_type(self, key, pos_tag):
        words = []
        for line in self.pos_files[key]:
            for element in line:
                if element[1] == pos_tag:
                    words.append(element[0].lower())
        return words

    def return_complex_ngram(self, key, args):
        ngram_length = len(args)
        complex_ngrams = []
        for line in self.pos_files[key]:
            for complex_ngram in nltk.ngrams(line, ngram_length):
                if self.check_complex_ngram(complex_ngram, ngram_length, args):
                    complex_ngrams.append(complex_ngram)
        return complex_ngrams

    def check_complex_ngram(self, complex_ngram, ngram_length, args):
        index = 0
        for word,tag in complex_ngram:
            if tag == None:
                return False
            if args[index] == '':
                word = ''
            if args[index].isupper():
                if tag != args[index]:
                    if tag.startswith(args[index]) == False:
                        return False
            else:
                if word != args[index]:
                    return False
            if index == ngram_length-1:
                return True
            index += 1
        return True