__author__ = 'Colin Sippl, Florian Fuchs'
# -*- coding: utf-8 -*-
from builtins import print
import nltk
from CorpusText import CorpusText
from nltk.collocations import *
from nltk.util import *
# http://stackoverflow.com/questions/7404720/nltk-fails-to-find-the-java-executable
import os

os.environ['JAVAHOME'] = "C:/Program Files/Java/jdk1.8.0_25/bin"

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

#Suchfenster für die N-Gramm-Extraktion
search_window = 5

#minimales Auftreten im Korpus
#4
min_freq = 3

args = [
    #Argumente für N-Gramm-Extraktion
    #N-Gramm-Typ, Länge, Extraktionsart, max. Anzahl, minimales Auftreten, Stoppwort-Verwendung
    #Extraktion der Bigramme
    #["bigram", bigram_measures.raw_freq, 300,  min_freq, True],
    ["bigram", bigram_measures.likelihood_ratio, 300,  min_freq, True],
    ["bigram", bigram_measures.poisson_stirling, 300, min_freq, True],
    ["bigram", bigram_measures.jaccard, 300,  min_freq, True],
    ["bigram", bigram_measures.pmi, 300,  min_freq, True],
    ["bigram", bigram_measures.chi_sq, 300,  min_freq, True],
    #Extraktion der Trigramme
    #["trigram", trigram_measures.raw_freq, 300,  min_freq, True],
    ["trigram", trigram_measures.likelihood_ratio, 300,  min_freq, True],
    ["trigram", trigram_measures.poisson_stirling, 300, min_freq, True],
    ["trigram", trigram_measures.jaccard, 300,  min_freq, True],
    ["trigram", trigram_measures.pmi, 300,  min_freq, True],
    ["trigram", trigram_measures.chi_sq, 300,  min_freq, True]
]

# http://streamhacker.com/tag/chi-square/
# http://www.nltk.org/howto/collocations.html
# http://www.nltk.org/api/nltk.metrics.html

class NgramFinder:


    @staticmethod
    def find(text, corpus_name, path_property):
        for entry in args:
            # Ignore stopwords
            NgramFinder._find_ngrams(entry[0], text, corpus_name, entry[1], entry[2], min_freq, True, path_property)
            # Leave stopwords
            #NgramFinder._find_ngrams(entry[0], text, corpus_name, entry[1], entry[2], min_freq, False)

    #http://stackoverflow.com/questions/5512765/removing-punctuation-numbers-from-text-problem


    @staticmethod
    def _create_finder(type, text):
        if type == "bigram":
            finder = BigramCollocationFinder.from_words(text, search_window)
        if type == "trigram":
            finder = TrigramCollocationFinder.from_words(text, search_window)
        return finder

    @staticmethod
    def _find_ngrams(type, text, corpus_name, method, maxhits, minhits, stopwordfilter, path_property):
        methodname = method.__name__
        if stopwordfilter:
            text = CorpusText._apply_stopwords(text)
        print("...Erstelle CollocationFinder-Objekt fuer Typ {" + type + ", " + methodname + "}...")
        finder = NgramFinder._create_finder(type, text)
        finder.apply_freq_filter(minhits)
        from CSVwriter import CSVwriter
        #print(finder.score_ngrams(method))
        CSVwriter.write_ngrams(methodname, corpus_name, stopwordfilter, minhits, maxhits, 'ngram', finder.score_ngrams(method), path_property)

    @staticmethod
    def _read_external_stopwords():
        return open("stopwords", encoding="utf8").read()

    @staticmethod
    def find_bigrams(corpus_text):
        return list(bigrams(corpus_text))

    @staticmethod
    def find_trigrams(corpus_text):
        return list(trigrams(corpus_text))


