from builtins import print
# -*- coding: utf-8 -*-
import nltk
from nltk.collocations import *
from nltk.util import *
# http://stackoverflow.com/questions/7404720/nltk-fails-to-find-the-java-executable
import os
import quadgramAssocMeasures
import re

os.environ['JAVAHOME'] = "C:/Program Files/Java/jdk1.8.0_25/bin"

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
quadgram_measures = quadgramAssocMeasures.QuadgramAssocMeasures()

#Suchfenster für die N-Gramm-Extraktion
search_window = 5

#minimales Auftreten im Korpus
min_freq = 4

args = [
    #Argumente für N-Gramm-Extraktion
    #N-Gramm-Typ, Länge, Extraktionsart, max. Anzahl, minimales Auftreten, Stoppwort-Verwendung
    #Extraktion der Bigramme
    #["bigram", bigram_measures.raw_freq, 300,  min_freq, True],
    ["bigram", bigram_measures.likelihood_ratio, 300,  min_freq, True],
    ["bigram", bigram_measures.poisson_stirling, 300, min_freq, True],
    ["bigram", bigram_measures.jaccard, 300,  min_freq, True],
    #["bigram", bigram_measures.pmi, 300,  min_freq, True],
    ["bigram", bigram_measures.chi_sq, 300,  min_freq, True],
    #Extraktion der Trigramme
    #["trigram", trigram_measures.raw_freq, 300,  min_freq, True],
    #["trigram", trigram_measures.likelihood_ratio, 300,  min_freq, True],
    #["trigram", trigram_measures.poisson_stirling, 300, min_freq, True],
    #["trigram", trigram_measures.jaccard, 300,  min_freq, True],
    #["trigram", trigram_measures.pmi, 300,  min_freq, True],
    #["trigram", trigram_measures.chi_sq, 300,  min_freq, True],
    #Extraktion der Quadgramme
    #["quadgram", quadgram_measures.raw_freq, 300,  min_freq, True],
    #["quadgram", quadgram_measures.likelihood_ratio, 300,  min_freq, True],
    #["quadgram", quadgram_measures.poisson_stirling, 300, min_freq, True],
    #["quadgram", quadgram_measures.jaccard, 300,  min_freq, True],
    #["quadgram", quadgram_measures.pmi, 300,  min_freq, True],
    #["quadgram", quadgram_measures.chi_sq, 300,  min_freq, True]
]

# http://streamhacker.com/tag/chi-square/
# http://www.nltk.org/howto/collocations.html
# http://www.nltk.org/api/nltk.metrics.html

class NgramFinder:

    #@staticmethod
    #def find(text, corpus_name):
    #    for entry in args:
    #        for i in range(1, min_freq+1):
    #            #Ignore stopwords
    #            NgramFinder._find_ngrams(entry[0], text, corpus_name, entry[1], entry[2], i, True)
    #            #Leave stopwords
    #            NgramFinder._find_ngrams(entry[0], text, corpus_name, entry[1], entry[2], i, False)

    @staticmethod
    def find(text, corpus_name):
        for entry in args:
            # Ignore stopwords
            NgramFinder._find_ngrams(entry[0], text, corpus_name, entry[1], entry[2], min_freq, True)
            # Leave stopwords
            #NgramFinder._find_ngrams(entry[0], text, corpus_name, entry[1], entry[2], min_freq, False)

    #http://stackoverflow.com/questions/5512765/removing-punctuation-numbers-from-text-problem

    @staticmethod
    def _clean_text(text):
        #text = [w.lower() for w in text]
        punctuation = re.compile(r'[.?!,„":;`€$\'()#|0-9]')
        return [punctuation.sub("", token) for token in text]

    @staticmethod
    def _create_finder(type, text):
        if type == "bigram":
            finder = BigramCollocationFinder.from_words(text, search_window)
        if type == "trigram":
            finder = TrigramCollocationFinder.from_words(text, search_window)
        if type == "quadgram":
            finder = nltk.collocations.QuadgramCollocationFinder.from_words(text, search_window)
        return finder

    @staticmethod
    def _find_ngrams(type, text, corpus_name, method, maxhits, minhits, stopwordfilter):
        methodname = method.__name__
        text = NgramFinder._clean_text(text)
        print("...Erstelle CollocationFinder-Objekt fuer Typ {" + type + ", " + methodname + "}...")
        finder = NgramFinder._create_finder(type, text)
        finder.apply_freq_filter(minhits)
        if stopwordfilter:
            ignored_words = nltk.corpus.stopwords.words('german')
            ignored_words2 = NgramFinder._read_external_stopwords()
            finder.apply_word_filter(lambda w: len(w) < 4 or w.lower() in ignored_words)
            finder.apply_word_filter(lambda w: len(w) < 4 or w.lower() in ignored_words2)
        from CSVwriter import CSVwriter
        CSVwriter.write_ngrams(methodname, corpus_name, stopwordfilter, minhits, maxhits, 'ngram', finder.score_ngrams(method))

    @staticmethod
    def _read_external_stopwords():
        return open("stopwords", encoding="utf8").read()

    @staticmethod
    def find_bigrams(corpus_text):
        return list(bigrams(corpus_text))

    @staticmethod
    def find_trigrams(corpus_text):
        return list(trigrams(corpus_text))


