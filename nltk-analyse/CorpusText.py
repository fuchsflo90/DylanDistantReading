__author__ = 'Colin Sippl'
# -*- coding: utf-8 -*-
import nltk
import math
from NgramFinder import NgramFinder

class CorpusText(object):

    @staticmethod
    def count_tokens(text):
        #print(text)
        return len(text)

    @staticmethod
    def count_unique_tokens(text):
        return len(set(text))

    @staticmethod
    def _apply_stopwords(text):
        text = [w.lower() for w in text]
        #ext_stopwords = CorpusText._read_external_stopwords()
        filter = nltk.corpus.stopwords.words('english')
        filter2 = (',', '.', '!', '?', ':', ';', '\xe2\x80\x94')
        #text = [w for w in text if w not in ext_stopwords]
        text = [w for w in text if w not in filter]
        text = [w for w in text if w not in filter2]
        return text

    @staticmethod
    def _apply_stopwords_to_pos(text):
        ext_stopwords = CorpusText._read_external_stopwords()
        filter = nltk.corpus.stopwords.words('german')
        filter2 = (',', '.', '!', '?', ':', ';', '\xe2\x80\x94')
        text = [(a,b) for (a,b) in text if a.lower() not in ext_stopwords]
        text = [(a,b) for (a,b) in text if a.lower() not in filter]
        text = [(a,b) for (a,b) in text if a.lower() not in filter2]
        return text

    @staticmethod
    def pos_rank_absolut_freq(stopwords, corpus_name, text, postag, filename):
        if stopwords:
            text = CorpusText._apply_stopwords_to_pos(text)
        freq = nltk.FreqDist(element[0].lower() for element in text if element[1] != None and element[1].startswith(postag))
        freq = list(freq.items())
        freq.sort(key=lambda tup: tup[1], reverse=True)
        from CSVwriter import CSVwriter
        CSVwriter.write_words_rank("word_rank_absolut_freq", corpus_name, stopwords, 300, "words", freq, filename)
        #freq.plot(50, cumulative=False)
        return freq

    @staticmethod
    def word_rank_absolut_freq(stopwords, corpus_name, text, filename):
        if stopwords:
            text = CorpusText._apply_stopwords(text)
        freq = nltk.FreqDist(word.lower() for word in text)
        freq = list(freq.items())
        freq.sort(key=lambda tup: tup[1], reverse=True)
        from CSVwriter import CSVwriter
        CSVwriter.write_words_rank("word_rank_absolut_freq", corpus_name, stopwords, 300, "words", freq, filename)
        #freq.plot(50, cumulative=False)
        return freq

    @staticmethod
    def bigrams_rank_absolut_freq(stopwords, corpus_name, text, filename):
        if stopwords:
            text = CorpusText._apply_stopwords(NgramFinder._clean_text(text))
        text = NgramFinder.find_bigrams(text)
        freq = nltk.FreqDist(text)
        freq = list(freq.items())
        freq.sort(key=lambda tup: tup[1], reverse=True)
        from CSVwriter import CSVwriter
        freq_list = []
        for entry in freq:
            freq_list.append((entry[0][0] + " " + entry[0][1], entry[1]))
        CSVwriter.write_words_rank("word_rank_absolut_freq", corpus_name, stopwords, 300, "words", freq_list, filename)
        #freq.plot(50, cumulative=False)
        return freq

    @staticmethod
    def trigrams_rank_absolut_freq(stopwords, corpus_name, text, filename):
        if stopwords:
            text = CorpusText._apply_stopwords(NgramFinder._clean_text(text))
        text = NgramFinder.find_trigrams(text)
        freq = nltk.FreqDist(text)
        freq = list(freq.items())
        freq.sort(key=lambda tup: tup[1], reverse=True)
        from CSVwriter import CSVwriter
        freq_list = []
        for entry in freq:
            freq_list.append((entry[0][0] + " " + entry[0][1] + " " + entry[0][2], entry[1]))
        CSVwriter.write_words_rank("word_rank_absolut_freq", corpus_name, stopwords, 300, "words", freq_list, filename)
        #freq.plot(50, cumulative=False)
        return freq

    @staticmethod
    def _read_external_stopwords():
        return open("stopwords", encoding="utf8").read()


    @staticmethod
    def _calculate_significant_word(freq_word_a, freq_word_b, n_tokens_text_a, n_tokens_text_b, word):
        """
        Rayson, P. and Garside, R. (2000). Comparing corpora using frequency profiling. In proceedings of the workshop
        on Comparing Corpora, held in conjunction with the 38th annual meeting of the Association for Computational
        Linguistics (ACL 2000). 1-8 October 2000, Hong Kong, pp. 1 - 6.

        http://ucrel.lancs.ac.uk/people/paul/publications/rg_acl2000.pdf
        """
        a = freq_word_a
        b = freq_word_b
        c = n_tokens_text_a
        d = n_tokens_text_b

        # Expectation I
        e_1 = c*(a+b) / (c+d)
        # Expectation II
        e_2 = d*(a+b) / (c+d)
        p = 2*((a*math.log(a/e_1)) + (b*math.log(b/e_2)))
        return (word, p)

    @staticmethod
    def calculate_significant_word_differences(fredDist_a, fredDist_b, tokens_length_a, tokens_length_b):
        fredDist_b = dict(fredDist_b)
        significant_difference_list = []
        for (a, b) in fredDist_a:
            if a in fredDist_b:
                if b > fredDist_b[a]:
                    significant_difference_list.append(CorpusText._calculate_significant_word(b, fredDist_b[a], tokens_length_a, tokens_length_b, a))
        significant_difference_list.sort(key=lambda tup: tup[1], reverse=True)
        return significant_difference_list

    @staticmethod
    def calculate_significant_bigram_differences(stopwords, corpus_a, corpus_b):
        if stopwords:
            #bigrams_a = NgramFinder.find_bigrams(CorpusText._apply_stopwords(NgramFinder._clean_text(corpus_a)))
            #bigrams_b = NgramFinder.find_bigrams(CorpusText._apply_stopwords(NgramFinder._clean_text(corpus_b)))
            bigrams_a = NgramFinder.find_bigrams(CorpusText._apply_stopwords(corpus_a))
            bigrams_b = NgramFinder.find_bigrams(CorpusText._apply_stopwords(corpus_b))
        else:
            bigrams_a = NgramFinder.find_bigrams(NgramFinder._clean_text(corpus_a))
            bigrams_b = NgramFinder.find_bigrams(NgramFinder._clean_text(corpus_b))
        length_a = len(bigrams_a)
        length_b = len(bigrams_b)
        freq_a = list(nltk.FreqDist(bigrams_a).items())
        freq_b = list(nltk.FreqDist(bigrams_b).items())
        freq_b = dict(freq_b)
        significant_difference_list = []
        for (a, b) in freq_a:
            if a in freq_b:
                 if b > freq_b[a]:
                    significant_difference_list.append(CorpusText._calculate_significant_word(b, freq_b[a], length_a, length_b, a[0] + " " + a[1]))
        significant_difference_list.sort(key=lambda tup: tup[1], reverse=True)
        return significant_difference_list

    @staticmethod
    def calculate_significant_trigram_differences(stopwords, corpus_a, corpus_b):
        if stopwords:
            trigrams_a = NgramFinder.find_trigrams(CorpusText._apply_stopwords(NgramFinder._clean_text(corpus_a)))
            trigrams_b = NgramFinder.find_trigrams(CorpusText._apply_stopwords(NgramFinder._clean_text(corpus_b)))
        else:
            trigrams_a = NgramFinder.find_trigrams(NgramFinder._clean_text(corpus_a))
            trigrams_b = NgramFinder.find_trigrams(NgramFinder._clean_text(corpus_b))
        length_a = len(trigrams_a)
        length_b = len(trigrams_b)
        freq_a = list(nltk.FreqDist(trigrams_a).items())
        freq_b = list(nltk.FreqDist(trigrams_b).items())
        freq_b = dict(freq_b)
        significant_difference_list = []
        for (a, b) in freq_a:
            if a in freq_b:
                 if b > freq_b[a]:
                    significant_difference_list.append(CorpusText._calculate_significant_word(b, freq_b[a], length_a, length_b, a[0] + " " + a[1] + " " + a[2]))
        significant_difference_list.sort(key=lambda tup: tup[1], reverse=True)
        return significant_difference_list



