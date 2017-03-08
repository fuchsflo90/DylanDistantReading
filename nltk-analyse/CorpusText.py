__author__ = 'Colin Sippl, Florian Fuchs'
# -*- coding: utf-8 -*-
import nltk
import math

class CorpusText(object):

    @staticmethod
    def count_tokens(text):
        return len(text)

    @staticmethod
    def count_unique_tokens(text):
        return len(set(text))

    @staticmethod
    def _apply_stopwords(text):
        ext_stopwords = CorpusText._read_external_stopwords()
        english_stopwords = nltk.corpus.stopwords.words('english')
        special_chars = (',', '.', '!', '?', ':', ';', '\xe2\x80\x94', '€', '$', '(', ')', '#', '|', "'", '"','`', '´')
        text = [(a,b) for (a,b) in text if a.lower() not in ext_stopwords]
        text = [(a,b) for (a,b) in text if a.lower() not in english_stopwords]
        text = [(a,b) for (a,b) in text if a not in special_chars]
        return text

    @staticmethod
    def pos_rank_absolut_freq(stopwords, corpus_name, text, postag, filename, path_property):
        #if stopwords:
        #    text = CorpusText._apply_stopwords(text)
        if postag == '':
            freq = nltk.FreqDist(
                element[0] for element in text)
        else:
            freq = nltk.FreqDist(element[0] for element in text if element[1] != None and element[1].startswith(postag))
        freq = list(freq.items())
        freq.sort(key=lambda tup: tup[1], reverse=True)
        #from CSVwriter import CSVwriter
        #CSVwriter.write_words_rank("word_rank_absolut_freq", corpus_name, stopwords, 300, "words", freq, filename, path_property)
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
        #print(fredDist_b)
        fredDist_b = dict(fredDist_b)
        significant_difference_list = []
        for (a, b) in fredDist_a:
            if a in fredDist_b:
                if b > fredDist_b[a]:
                    significant_difference_list.append(CorpusText._calculate_significant_word(b, fredDist_b[a], tokens_length_a, tokens_length_b, a))
        significant_difference_list.sort(key=lambda tup: tup[1], reverse=True)
        return significant_difference_list
