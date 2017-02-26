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

    dylanIsOnlyAuthor = True
    allAuthors = False
    intervalls = [
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Brown, D. (2014). Bob Dylan: American troubadour. Lanham, Md. [u.a.]: Rowman & Littlefield.

        # Becoming Bob Dylan
        (1960, 1964, dylanIsOnlyAuthor),
        (1960, 1964, allAuthors),

        # Electric Dylan
        (1965, 1966, dylanIsOnlyAuthor),
        (1965, 1966, allAuthors),

        # Rural Glory
        (1967, 1967, dylanIsOnlyAuthor),
        (1967, 1967, allAuthors),

        # "Take Me As I Am"
        (1968, 1973, dylanIsOnlyAuthor),
        (1968, 1973, allAuthors),

        # Back in the Rain
        (1974, 1978, dylanIsOnlyAuthor),
        (1974, 1978, allAuthors),

        # The Changing of the Guard
        (1978, 1981, dylanIsOnlyAuthor),
        (1978, 1981, allAuthors),

        # Rock and Roll Dreams
        (1983, 1990, dylanIsOnlyAuthor),
        (1983, 1990, allAuthors),

        # Good Enough for Now
        (1989, 1997, dylanIsOnlyAuthor),
        (1989, 1997, allAuthors),

        # Bob Dylan Revisited
        (2000, 2012, dylanIsOnlyAuthor),
        (2000, 2012, allAuthors),

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Gesamtkorpus 1960 bis Gegenwart
        (1960, 2019, dylanIsOnlyAuthor),
        (1960, 2019, allAuthors),

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Dekaden
        (1960, 1969, dylanIsOnlyAuthor), (1960, 1969, allAuthors),
        (1970, 1979, dylanIsOnlyAuthor), (1970, 1979, allAuthors),
        (1980, 1989, dylanIsOnlyAuthor), (1980, 1989, allAuthors),
        (1990, 1999, dylanIsOnlyAuthor), (1990, 1999, allAuthors),
        (2000, 2009, dylanIsOnlyAuthor), (2000, 2009, allAuthors),
        (2010, 2019, dylanIsOnlyAuthor), (2010, 2019, allAuthors),

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Dylans Selbstfindung
        (1964, 1965, dylanIsOnlyAuthor), (1964, 1965, allAuthors),

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Sonstiges
        (1965, 1970, dylanIsOnlyAuthor), (1965, 1970, allAuthors),

        ]

    #st = SnowballStemmer("english", ignore_stopwords=True)
    st = SnowballStemmer("english")

    for decade in intervalls:

        year_start = decade[0]
        year_end = decade[1]
        authorship = decade[2]

        path_spec = ""
        if authorship == True:
            path_spec = "dylan_"
        if authorship == False:
            path_spec = "all_"

        path_property = str(year_start) + '-' + str(year_end)

        # *****************************************Erstelle Untersuchungskorpora********************************************#
        corpora = reader.select_taggedsongs_from_author(authorship, year_start, year_end)


        #print(corpora[1])
        print("Anzahl der Tokens des Untersuchungskorpus: " + str(len(corpora[0])))
        print("Anzahl der Tokens des Kontrollkorpus: " + str(len(corpora[1])))

        untersuchungsbereich = CorpusText._apply_stopwords([ ( (st.stem(a)) ,b) for (a,b) in corpora[0] ])
        kontrollbereich = CorpusText._apply_stopwords([ ( (st.stem(a)) ,b) for (a,b) in corpora[1] ])

        # *************************************Erstelle Metafinormationen zu den Korpora************************************#
        length_a = CorpusText.count_tokens(untersuchungsbereich)
        length_b = CorpusText.count_tokens(kontrollbereich)

        # ******Stoppwortliste: JA
        fredDist_a = CorpusText.pos_rank_absolut_freq(True, path_spec + "int", untersuchungsbereich, "", 'all_words',
                                                      path_property)
        fredDist_b = CorpusText.pos_rank_absolut_freq(True, path_spec + "rest", kontrollbereich, "", 'all_words', path_property)

        difvals = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
        CSVwriter.write_text_differences("significant_text_differences", path_spec + "int", True, 300, "words", difvals,
                                         'all_words', path_property)

        #*****************************************************Dylan vs. OANC **********************************************#
        #*************************************************** + LEMMATISIERUNG + *******************************************#

        #st = LancasterStemmer()
        #st = SnowballStemmer("english")
        #untersuchungsbereich_lem = [ ( (st.stem(a)) ,b) for (a,b) in untersuchungsbereich ]

        n_lexems_dylan = CorpusText.count_tokens(untersuchungsbereich)
        #print(str( n_lexems_dylan ) + " vs. " + str(length_a))
        #print(untersuchungsbereich_lem)
        fredDist_lem = CorpusText.pos_rank_absolut_freq(True, path_spec + "int", untersuchungsbereich, "", 'all_words',
                                                      path_property)

        fredDist_anc = FileReader.read_ANC_file(anc_all_count, 1, 3)
        #print(fredDist_anc)
        total_anc_words = sum(val[1] for val in fredDist_anc)
        difvals = CorpusText.calculate_significant_word_differences(fredDist_lem, fredDist_anc,  n_lexems_dylan, total_anc_words)
        CSVwriter.write_text_differences("significant_text_differences", path_spec + "anc", True, 300, "words", difvals,
                                         'all_words', path_property)

        # ******************************************************************************************************************#

        # Signifikante Unterschiede der Worthäufigkeiten (Wortartenfilterung)
        args = [('NN', 'nouns'), ('NNP', 'proper_nouns'), ('VB', 'verbs'), ('JJ', 'adjectives')]

        for arg in args:
            # with stopwords
            fredDist_a = CorpusText.pos_rank_absolut_freq(True, path_spec + "int", untersuchungsbereich, arg[0], arg[1],
                                                          path_property)
            fredDist_b = CorpusText.pos_rank_absolut_freq(True, path_spec + "rest", kontrollbereich, arg[0], arg[1],
                                                          path_property)
            difvals2 = CorpusText.calculate_significant_word_differences(fredDist_a, fredDist_b, length_a, length_b)
            CSVwriter.write_text_differences("significant_text_differences", path_spec + "int", True, 300, "words", difvals2,
                                             arg[1], path_property)
            #print(length_a)
        # Signifikanzvergleich zum OANC (lemmatisiert)
            fredDist_lem = CorpusText.pos_rank_absolut_freq(True, path_spec + "int", untersuchungsbereich, arg[0], arg[1],
                                                            path_property)

            difvals = CorpusText.calculate_significant_word_differences(fredDist_lem, fredDist_anc, n_lexems_dylan,
                                                                        total_anc_words)
            CSVwriter.write_text_differences("significant_text_differences", path_spec + "anc", True, 300, "words", difvals,
                                             arg[1], path_property)

            # vice versa
            # difvals2 = CorpusText.calculate_significant_word_differences(fredDist_b, fredDist_a, length_b, length_a)
            # CSVwriter.write_text_differences("significant_text_differences", "dylan_rest", True, 300, "words", difvals2, arg[1], path_property)

        # ******************************************************Finde N-Gramme**********************************************#
        # *****************************************************!!!!ACHTUNG!!!!**********************************************#
        # *****************************Berechungszeit kann unter Umständen sehr lange dauern!!!*****************************#
        # Details siehe Klasse NgramFinder
        NgramFinder.find(untersuchungsbereich, path_spec + "int", path_property)
        # NgramFinder.find(corpus_b, name_b)

if __name__ == '__main__':
    print('This program is being run by itself')
    main()
else:
    print('I am being imported from another module')