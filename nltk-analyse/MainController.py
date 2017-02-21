__author__ = 'Colin Sippl, Florian Fuchs'
# -*- coding: utf-8 -*-
# lese Songtext-Korpusdatei
from CorpusText import CorpusText
from CSVwriter import CSVwriter
from NgramFinder import NgramFinder
from FileReader import FileReader
from CorpusReader import CorpusReader
from nltk.stem.snowball import SnowballStemmer

# Name der Korpusdatei
file_name = "Corpus_Dylan452.xml"
# Pfad der Korpusdatei
corpus_path = './corpus/'

# OANC-Referenzkorpus-Dateien
anc_token_count = './corpus/ANC/ANC-token-count.txt'
# Lemmata u. POS-Tags enthalten
anc_written_count = './corpus/ANC/ANC-written-count.txt'
anc_spoken_count = './corpus/ANC/ANC-spoken-count.txt'
anc_all_count = './corpus/ANC/ANC-all-count.txt'

def main():
    # ************************************************Lese Dylan-Korpusdatei********************************************#
    reader = CorpusReader(file_name, corpus_path)
    reader.read_file()
    reader.parse_file()

    # **********************************Untersuchungsintervalle v. Dylans Werk******************************************#
    # intervalls = [(1960, 1970), (1971, 1980), (1981, 1990), (1991, 2000), (2001, 2020)]
    year_start = 2000
    year_end = 2020
    year_end_corpus = 2020

    path_property = str(year_start) + '-' + str(year_end)

    # *****************************************Erstelle Untersuchungskorpora********************************************#
    untersuchungsbereich = reader.select_taggedsongs_from_author("Bob Dylan", year_start, year_end)
    # print(untersuchungsbereich)
    kontrollbereich = reader.select_taggedsongs_from_author("Bob Dylan", year_end + 1, year_end_corpus)
    # kontrollbereich = nltk.word_tokenize(kontrollbereich)

    # *************************************Erstelle Metafinormationen zu den Korpora************************************#
    length_a = CorpusText.count_tokens(untersuchungsbereich)
    length_b = CorpusText.count_tokens(kontrollbereich)
    # print("Anzahl der Tokens des Untersuchungskorpus: " + str(length_a))
    # print("Anzahl der Tokens des Untersuchungskorpus: " + str(len(CorpusText.pos_rank_absolut_freq(False, "dylan_int", untersuchungsbereich, "", "test"))))
    # print("Anzahl der Tokens des Vergleichskorpus: " + str(length_b))

    # ******Stoppwortliste: JA
    fredDist_a = CorpusText.pos_rank_absolut_freq(True, "dylan_int", untersuchungsbereich, "", 'all_words',
                                                  path_property)
    fredDist_b = CorpusText.pos_rank_absolut_freq(True, "dylan_rest", kontrollbereich, "", 'all_words', path_property)

    difvals = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
    CSVwriter.write_text_differences("significant_text_differences", "dylan_int", True, 300, "words", difvals,
                                     'all_words', path_property)
    # vice versa
    # difvals = CorpusText.calculate_significant_word_differences(fredDist_b, fredDist_a,
    #                                                     length_a, length_b)
    # CSVwriter.write_text_differences("significant_text_differences", "dylan_rest", True, 300, "words", difvals, 'all_words', path_property)

    # print([token[0] for token in untersuchungsbereich])

    #*****************************************************Dylan vs. OANC **********************************************#
    #*************************************************** + LEMMATISIERUNG + *******************************************#

    #st = LancasterStemmer()
    st = SnowballStemmer("english")
    untersuchungsbereich_lem = [ ( (st.stem(a)) ,b) for (a,b) in untersuchungsbereich ]
    n_lexems_dylan = CorpusText.count_tokens(untersuchungsbereich_lem)
    #print(str( n_lexems_dylan ) + " vs. " + str(length_a))
    #print(untersuchungsbereich_lem)
    fredDist_lem = CorpusText.pos_rank_absolut_freq(True, "dylan_int", untersuchungsbereich_lem, "", 'all_words',
                                                  path_property)

    fredDist_anc = FileReader.read_ANC_file(anc_all_count, 1, 3)
    #print(fredDist_anc)
    total_anc_words = sum(val[1] for val in fredDist_anc)
    difvals = CorpusText.calculate_significant_word_differences(fredDist_lem, fredDist_anc,  n_lexems_dylan, total_anc_words)
    CSVwriter.write_text_differences("significant_text_differences", "dylan_anc", True, 300, "words", difvals,
                                     'all_words', path_property)

    # ******************************************************************************************************************#

    # Signifikante Unterschiede der Worthäufigkeiten (Wortartenfilterung)
    args = [('NN', 'nouns'), ('NNP', 'proper_nouns'), ('VB', 'verbs'), ('JJ', 'adjectives')]

    for arg in args:
        # with stopwords
        fredDist_a = CorpusText.pos_rank_absolut_freq(True, "dylan_int", untersuchungsbereich, arg[0], arg[1],
                                                      path_property)
        fredDist_b = CorpusText.pos_rank_absolut_freq(True, "dylan_rest", kontrollbereich, arg[0], arg[1],
                                                      path_property)
        difvals2 = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
        CSVwriter.write_text_differences("significant_text_differences", "dylan_int", True, 300, "words", difvals2,
                                         arg[1], path_property)
        # vice versa
        # difvals2 = CorpusText.calculate_significant_word_differences(fredDist_b, fredDist_a, length_b, length_a)
        # CSVwriter.write_text_differences("significant_text_differences", "dylan_rest", True, 300, "words", difvals2, arg[1], path_property)

    # ******************************************************Finde N-Gramme**********************************************#
    # *****************************************************!!!!ACHTUNG!!!!**********************************************#
    # *****************************Berechungszeit kann unter Umständen sehr lange dauern!!!*****************************#
    # Details siehe Klasse NgramFinder
    NgramFinder.find(untersuchungsbereich, "dylan_int", path_property)
    # NgramFinder.find(corpus_b, name_b)

if __name__ == '__main__':
    print('This program is being run by itself')
    main()
else:
    print('I am being imported from another module')