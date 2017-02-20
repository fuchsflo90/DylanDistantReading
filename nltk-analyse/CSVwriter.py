__author__ = 'Colin Sippl'
# -*- coding: utf-8 -*-
import os

class CSVwriter(object):
    @staticmethod
    def write_ngrams(method_name, corpus_name, stopwordfilter, minhits, maxlength, datatype, data):
        ngram_length = len(data[0][0])
        #print("Gesamt: " + str(len(data)) + " Reihe 1: " + str(ngram_length))
        path = './output/data/' + datatype + '/' + 'min' + str(minhits) + '/' + corpus_name + '/' + 'stopwords_' + str(stopwordfilter) + '/' + method_name + '/'
        print("___________________Erzeuge " + datatype + '/' + 'min' + str(minhits) + '/' + corpus_name + '/' + 'stopwords_' + str(stopwordfilter) + '/' + method_name + '/' + str(ngram_length) +'-gram.csv')
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + str(ngram_length) +'-gram.csv', mode='w', encoding='utf8') as csv_file:
            csv_file.write('NGRAM,VALUE,\n')
            if maxlength > len(data)-1:
                maxlength = len(data)-1
            for element in data[:maxlength]:
                try:
                    out = ""
                    index = 0
                    for e in element[0]:
                        if index == ngram_length-1:
                            out += str(e[0])
                        else:
                            out += str(e[0]) + " "
                        index += 1
                    out += "," + str(element[1]) + "\n"
                    csv_file.write(out)
                except (UnicodeEncodeError):
                    print("ERROR__________________________________")
                    pass
            csv_file.close()

    @staticmethod
    def write_text_differences(method_name, corpus_name, stopwordfilter, maxlength, datatype, data, filename):
        path = './output/data/' + datatype + '/' + corpus_name + '/' + 'stopwords_' + str(stopwordfilter) + '/' + method_name + '/'
        print("___________________Erzeuge " + datatype + '/' + corpus_name + '/' + 'stopwords_' + str(stopwordfilter) + '/' + method_name + '/' + filename +'.csv')
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + filename +'.csv', mode='w', encoding='utf8') as csv_file:
            csv_file.write('WORD,VALUE,\n')
            for element in data[:maxlength]:
                try:
                    csv_file.write(element[0] + "," + str(element[1]) + "\n")
                except (UnicodeEncodeError):
                    print("ERROR__________________________________")
                    pass
            csv_file.close()

    @staticmethod
    def write_context(method_name, corpus_name, maxlength, datatype, data):
        path = './output/data/' + datatype + '/' + corpus_name + '/' + method_name + '/'
        print("___________________Erzeuge " + datatype + '/' + corpus_name + '/' + method_name + '/' + data[0][0] +'.csv')
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + data[0][0] +'.csv', mode='w', encoding='utf8') as csv_file:
            csv_file.write('WORD,VALUE,\n')
            for element in data[:maxlength]:
                try:
                    csv_file.write(element[0] + "," + str(element[1]) + "\n")
                except (UnicodeEncodeError):
                    print("ERROR__________________________________")
                    pass
            csv_file.close()

    @staticmethod
    def write_words_rank(method_name, corpus_name, stopwordfilter, maxlength, datatype, data, filename):
        path = './output/data/' + datatype + '/' + corpus_name + '/' + 'stopwords_' + str(stopwordfilter) + '/' + method_name + '/'
        print("___________________Erzeuge " + datatype + '/' + corpus_name + '/'  + 'stopwords_' + str(stopwordfilter) + '/' + method_name + '/' + filename +'.csv')
        if not os.path.exists(path):
            os.makedirs(path)
        with open(path + filename +'.csv', mode='w', encoding='utf8') as csv_file:
            csv_file.write('WORD,RANK,\n')
            for element in data[:maxlength]:
                try:
                    csv_file.write(element[0] + "," + str(element[1]) + "\n")
                except (UnicodeEncodeError):
                    print("ERROR__________________________________")
                    pass
            csv_file.close()

