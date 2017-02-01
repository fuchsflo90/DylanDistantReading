__author__ = 'Colin Sippl'
# -*- coding: utf-8 -*-
from FileReader import FileReader
from POSManager import POSManager
from CorpusText import CorpusText
from NgramFinder import NgramFinder
from JSONWriter import JSONWriter
from nltk import ContextIndex
from CSVwriter import CSVwriter
import math

#Vergleichspartei a)
name_a = "fp\xf6_XXV"
#Vergleichspartei b)
name_b = "gr\xfcne_XXV"
#name_b = "glawischnig"
corpus_path = './corpus/'

#Tagset: http://www.ims.uni-stuttgart.de/forschung/ressourcen/lexika/TagSets/stts-table.html

def main():
    #***********************************************Lese Korpusdateien ein**********************************************
    #************************************Erstelle Metafinormationen zu den Korpora**************************************
    reader_a = FileReader(name_a, corpus_path)
    reader_b = FileReader(name_b, corpus_path)

    # Parse POS-Korpus-Dateien
    pos_manager = POSManager()
    pos_manager.add_corpus_files(name_a, reader_a.return_pos_file(), reader_a.return_raw_text_lines())
    pos_manager.add_corpus_files(name_b, reader_b.return_pos_file(), reader_b.return_raw_text_lines())

    # Ausgabe der Korpus-Texte tokenisiert
    corpus_a = reader_a.return_raw_text_tokens()
    #corpus_a = reader_a.return_pos_file()
    corpus_b = reader_b.return_raw_text_tokens()
    #corpus_b = reader_a.return_pos_file()

    # Berechne Anzahl der Tokens pro Korpus-Text
    length_a = CorpusText.count_tokens(corpus_a)
    length_b = CorpusText.count_tokens(corpus_b)

    #Metafinormationen zu den Korpora
    # Name, Tokens, Sätze
    meta_info = {}
    meta_info['partei_a'] = {'name' : name_a, 'tokens':length_a, 'sentences' : len(reader_a.return_raw_text_lines()),
                             'corpus' : './corpus/'+ name_a + '.txt', 'pos' : './corpus/POS_' + name_a + '.txt'}
    meta_info['partei_b'] = {'name' : name_b, 'tokens':length_b, 'sentences' : len(reader_b.return_raw_text_lines()),
                             'corpus' : './corpus/'+ name_b + '.txt', 'pos' : './corpus/POS_' + name_b + '.txt'}
    meta_info['general'] = {'tagger': 'Stanford NLP German-DEWAC', 'gp' : 'XXV', 'beginn' : '16.12.2013'}
    JSONWriter.writeJSONData(meta_info)

    #*****************************************LOG-LIKELIHOOD KORPUSVERGLEICH********************************************
    #*******************************         Vergleich der Worthäufigkeiten         ************************************
    #*******************************      Vergleich der Wortartenhäufigkeiten(POS)  ************************************
    #*******************************Vergleich der Bigramm- und Trigramm-Häufigkeiten************************************
    #CorpusText.bigrams_rank_absolut_freq(False, name_a, corpus_a, 'bigrams')
    #CorpusText.bigrams_rank_absolut_freq(False, name_b, corpus_b, 'bigrams')
    #CorpusText.bigrams_rank_absolut_freq(True, name_a, corpus_a, 'bigrams')
    #CorpusText.bigrams_rank_absolut_freq(True, name_b, corpus_b, 'bigrams')

    # CorpusText.trigrams_rank_absolut_freq(False, name_a, corpus_a, 'trigrams')
    # CorpusText.trigrams_rank_absolut_freq(False, name_b, corpus_b, 'trigrams')
    # CorpusText.trigrams_rank_absolut_freq(True, name_a, corpus_a, 'trigrams')
    # CorpusText.trigrams_rank_absolut_freq(True, name_b, corpus_b, 'trigrams')

    #Bigramme
    #*****Stoppwortliste: NEIN
    difvals = CorpusText.calculate_significant_bigram_differences(False, corpus_a, corpus_b)
    CSVwriter.write_text_differences("significant_text_differences", name_a, False, 300, "words", difvals, 'bigrams')
    difvals = CorpusText.calculate_significant_bigram_differences(False, corpus_b, corpus_a)
    CSVwriter.write_text_differences("significant_text_differences", name_b, False, 300, "words", difvals, 'bigrams')

    #*****Stoppwortliste: JA
    difvals = CorpusText.calculate_significant_bigram_differences(True, corpus_a, corpus_b)
    CSVwriter.write_text_differences("significant_text_differences", name_a, True, 300, "words", difvals, 'bigrams')
    difvals = CorpusText.calculate_significant_bigram_differences(True, corpus_b, corpus_a)
    CSVwriter.write_text_differences("significant_text_differences", name_b, True, 300, "words", difvals, 'bigrams')

    #Trigramme
    #*****Stoppwortliste: NEIN
    #difvals = CorpusText.calculate_significant_trigram_differences(False, corpus_a, corpus_b)
    #CSVwriter.write_text_differences("significant_text_differences", name_a, False, 300, "words", difvals, 'trigrams')
    #difvals = CorpusText.calculate_significant_trigram_differences(False, corpus_b, corpus_a)
    #CSVwriter.write_text_differences("significant_text_differences", name_b, False, 300, "words", difvals, 'trigrams')

    #*****Stoppwortliste: JA
    #difvals = CorpusText.calculate_significant_trigram_differences(True, corpus_a, corpus_b)
    #CSVwriter.write_text_differences("significant_text_differences", name_a, True, 300, "words", difvals, 'trigrams')
    #difvals = CorpusText.calculate_significant_trigram_differences(True, corpus_b, corpus_a)
    #CSVwriter.write_text_differences("significant_text_differences", name_b, True, 300, "words", difvals, 'trigrams')

    #Signifikante Unterschiede der Worthäufigkeiten (alle Wortarten)
    #*****Stoppwortliste: NEIN
    fredDist_a_no_stopwords = CorpusText.word_rank_absolut_freq(False, name_a, corpus_a, 'all_words')
    fredDist_b_no_stopwords = CorpusText.word_rank_absolut_freq(False, name_b, corpus_b, 'all_words')

    difvals = CorpusText.calculate_significant_word_differences(fredDist_a_no_stopwords, fredDist_b_no_stopwords, length_a, length_b)
    CSVwriter.write_text_differences("significant_text_differences", name_a, False, 300, "words", difvals, 'all_words')
    # vice versa
    difvals = CorpusText.calculate_significant_word_differences(fredDist_b_no_stopwords, fredDist_a_no_stopwords, length_a, length_b)
    CSVwriter.write_text_differences("significant_text_differences", name_b, False, 300, "words", difvals, 'all_words')

    #*****Stoppwortliste: JA
    fredDist_a = CorpusText.word_rank_absolut_freq(True, name_a, corpus_a, 'all_words')
    fredDist_b = CorpusText.word_rank_absolut_freq(True, name_b, corpus_b, 'all_words')

    difvals = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
    CSVwriter.write_text_differences("significant_text_differences", name_a, True, 300, "words", difvals, 'all_words')
    # vice versa
    difvals = CorpusText.calculate_significant_word_differences(fredDist_b, fredDist_a, length_b, length_a)
    CSVwriter.write_text_differences("significant_text_differences", name_b, True, 300, "words", difvals, 'all_words')

    #Signifikante Unterschiede der Worthäufigkeiten (Wortartenfilterung)
    # args = [('N', 'nouns'),('NE', 'nouns_ne'),('NN', 'nouns_nn'),('VVINF', 'verbs_inf'),('VVIZU', 'verbs_zu'),
    #         ('VVIMP', 'verbs_imp'), ('VM', 'verbs_mod'), ('PPOS', 'pronouns_pos'), ('ADJ', 'adjectives'),
    #         ('ADJA', 'adjectives_at'),('CARD', 'numbers'), ('FM', 'fm'), ('ADJD', 'adjectives_ad')]
    #
    # for arg in args:
    #     #without stopwords
    #     fredDist_a = CorpusText.pos_rank_absolut_freq(False, name_a, reader_a.return_tagged_tokens(), arg[0], arg[1])
    #     fredDist_b = CorpusText.pos_rank_absolut_freq(False, name_b, reader_b.return_tagged_tokens(), arg[0], arg[1])
    #     difvals2 = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
    #     CSVwriter.write_text_differences("significant_text_differences", name_a, False, 300, "words", difvals2, arg[1])
    #     # vice versa
    #     difvals2 = CorpusText.calculate_significant_word_differences(fredDist_b, fredDist_a, length_b, length_a)
    #     CSVwriter.write_text_differences("significant_text_differences", name_b, False, 300, "words", difvals2, arg[1])
    #
    #     #with stopwords
    #     fredDist_a = CorpusText.pos_rank_absolut_freq(True, name_a, reader_a.return_tagged_tokens(), arg[0], arg[1])
    #     fredDist_b = CorpusText.pos_rank_absolut_freq(True, name_b, reader_b.return_tagged_tokens(), arg[0], arg[1])
    #     difvals2 = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
    #     CSVwriter.write_text_differences("significant_text_differences", name_a, True, 300, "words", difvals2, arg[1])
    #     # vice versa
    #     difvals2 = CorpusText.calculate_significant_word_differences(fredDist_b, fredDist_a, length_b, length_a)
    #     CSVwriter.write_text_differences("significant_text_differences", name_b, True, 300, "words", difvals2, arg[1])


    #*************************************************Gemeinsamer Wortkontext*******************************************
    #Keine Implementierung in der Web-Darstellung
    #http://stackoverflow.com/questions/14287993/words-generated-from-text-similar-and-contextindex-similar-words-in-nltk-sor
    """
    c_list = ContextIndex(reader_a.return_raw_text_tokens())
    c_word = c_list.word_similarity_dict('Asylwerber')
    c_word = sorted(c_word.items(), key=lambda word: word[1], reverse=True)
    CSVwriter.write_context("word_similarity_dict", name_a, 10, "context", c_word)

    c_list = ContextIndex(reader_b.return_raw_text_tokens())
    c_word = c_list.word_similarity_dict('Asylwerber')
    c_word = sorted(c_word.items(), key=lambda word: word[1], reverse=True)
    CSVwriter.write_context("word_similarity_dict", name_b, 10, "context", c_word)
    """

    #******************************************************Finde N-Gramme***********************************************
    #*****************************************************!!!!ACHTUNG!!!!***********************************************
    #*****************************Berechungszeit kann unter Umständen länger als 24h dauern!!!**************************
    # Details siehe Klasse NgramFinder
    NgramFinder.find(corpus_a, name_a)
    NgramFinder.find(corpus_b, name_b)


    #******************************************************Wortformengruppen********************************************
    # Keine Implementierung in der Web-Darstellung
    # word_pattern = ('die', 'Zahl', 'der', 'N')
    # Kampf gegen X
    # wir sind in
    # wir sind f\xfcr
    # vgl. Bubenhofer (2009;2013) "Sprachgebrauchsmuster"
    # http://mbostock.github.io/d3/talk/20111018/tree.html
    """
    word_pattern = ('Kampf', 'gegen', 'ART', 'NN')
    ngrams = pos_manager.return_complex_ngram(name_a, word_pattern)
    print_ngrams(ngrams)
    ngrams = pos_manager.return_complex_ngram(name_b, word_pattern)
    print_ngrams(ngrams)
    word_pattern = ('Kampf', 'gegen', 'NN')
    ngrams = pos_manager.return_complex_ngram(name_a, word_pattern)
    print_ngrams(ngrams)
    ngrams = pos_manager.return_complex_ngram(name_b, word_pattern)
    print_ngrams(ngrams)
    """



def print_ngrams(ngrams):
    for line in ngrams:
        ngramstring = ""
        grammastring = ""
        for a, b in line:
            ngramstring = ngramstring + a + " "
            grammastring = grammastring + b + " "
        print(ngramstring)
        print(grammastring)
        print("\n")


if __name__ == '__main__':
    print('This program is being run by itself')
    main()
else:
    print('I am being imported from another module')