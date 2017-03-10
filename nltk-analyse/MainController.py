# -*- coding: utf-8 -*-
"""
In dieser Klasse findet die zentrale Steuerung der Komponenten statt, die die Berechnung und Erzeugung
der Ausgabedateien (CSV) kontrollieren.

Die Einteilung v. Dylans Schaffensphasen erfolgt nach

    - Brown, D. (2014). Bob Dylan: American troubadour. Lanham, Md. [u.a.]: Rowman & Littlefield.
    - Dekaden



"""
__author__ = 'Colin Sippl, Florian Fuchs'
from CorpusText import CorpusText
from CSVwriter import CSVwriter
from NgramFinder import NgramFinder
from FileReader import FileReader
from CorpusReader import CorpusReader
#from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Name der Korpusdatei
file_name = "Corpus_Dylan_Twitter452.xml"
#file_name = "Corpus_Dylan452.xml"

# Pfad der Korpusdatei
corpus_path = './corpus/'

# OANC-Referenzkorpus-Dateien
# anc_token_count = './corpus/ANC/ANC-token-count.txt'
# anc_written_count = './corpus/ANC/ANC-written-count.txt'
oanc_corpus = './corpus/ANC/ANC-spoken-count.txt'
# oanc_corpus = './corpus/ANC/ANC-all-count.txt'

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

        # Becoming Bob Dylan (1960 - 1964)
        (1960, 1964, dylanIsOnlyAuthor),
        (1960, 1964, allAuthors),

        # Electric Dylan (1965 - 1966)
        (1965, 1966, dylanIsOnlyAuthor),
        (1965, 1966, allAuthors),

        # Rural Glory (1967)
        (1967, 1967, dylanIsOnlyAuthor),
        (1967, 1967, allAuthors),

        # "Take Me As I Am" (1968 - 1973)
        (1968, 1973, dylanIsOnlyAuthor),
        (1968, 1973, allAuthors),

        # Back in the Rain (1974 - 1978)
        (1974, 1978, dylanIsOnlyAuthor),
        (1974, 1978, allAuthors),

        # The Changing of the Guard (1978 - 1981)
        (1978, 1981, dylanIsOnlyAuthor),
        (1978, 1981, allAuthors),

        # Rock and Roll Dreams (1983 - 1990)
        (1983, 1990, dylanIsOnlyAuthor),
        (1983, 1990, allAuthors),

        # Good Enough for Now (1989 - 1997)
        (1989, 1997, dylanIsOnlyAuthor),
        (1989, 1997, allAuthors),

        # Bob Dylan Revisited (2000 - 2012)
        (2000, 2012, dylanIsOnlyAuthor),
        (2000, 2012, allAuthors),

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Wissolik, R. D., McGrath, S., & Colaianne, A. J. (1994). Bob Dylan’s words:
        # a critical dictionary and commentary. Greensburg, PA: Eadmer Press.

        #(1962, 1985, dylanIsOnlyAuthor),
        #(1962, 1985, allAuthors),

        # Optional: Möglichkeit zur Anzeige dieser Daten ist in der Webapp ausgeblendet
        # Keine nähere Erläuterung in der Dokumentation dieses Projekts

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Gesamtkorpus 1960 bis Gegenwart, daher Intervall bis '2019'
        (1960, 2019, dylanIsOnlyAuthor),
        (1960, 2019, allAuthors),

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Dekaden
        # Auch wenn sich Dylans Schaffensphasen nicht wirklich an Dekaden-Grenzen halten,
        # ist eine Betrachtung der einzelnen Jahrzehnte ebenfalls interessant, insbesondere
        # mit Blick auf die 1960er oder die Gegenwart
        (1960, 1969, dylanIsOnlyAuthor), (1960, 1969, allAuthors),
        (1970, 1979, dylanIsOnlyAuthor), (1970, 1979, allAuthors),
        (1980, 1989, dylanIsOnlyAuthor), (1980, 1989, allAuthors),
        (1990, 1999, dylanIsOnlyAuthor), (1990, 1999, allAuthors),
        (2000, 2009, dylanIsOnlyAuthor), (2000, 2009, allAuthors),
        (2010, 2019, dylanIsOnlyAuthor), (2010, 2019, allAuthors),

        ]

    # *****************************************Stemming und Lemmatisierung********************************************#

    #st = SnowballStemmer("english", ignore_stopwords=True)
    #st = SnowballStemmer("english")

    wordnet_lemmatizer = WordNetLemmatizer()

    # *****************************************STARTE ANALYSE DES DYLAN-KORPUS********************************************#

    for decade in intervalls:
        year_start = decade[0]
        year_end = decade[1]
        authorship = decade[2]
        print("#*******************************************|    Berechne: " + str(year_start) + " bis " + str(year_end) + " für alle " + str(authorship))

        path_spec = ""
        if authorship == True:
            path_spec = "dylan_"
        if authorship == False:
            path_spec = "all_"

        path_property = str(year_start) + '-' + str(year_end)

        # *****************************************Erstelle Untersuchungskorpora********************************************#
        corpora = reader.select_taggedsongs_from_author(authorship, year_start, year_end)

        print("Anzahl der Tokens des Untersuchungskorpus: " + str(len(corpora[0])))
        print("Anzahl der Tokens des Kontrollkorpus: " + str(len(corpora[1])))

        untersuchungsbereich = CorpusText._apply_stopwords([ ( (wordnet_lemmatizer.lemmatize(normalize_token(a,b), pos=get_wordnet_pos(b))) ,b) for (a,b) in corpora[0] ])
        kontrollbereich = CorpusText._apply_stopwords([ ( (wordnet_lemmatizer.lemmatize(normalize_token(a,b), pos=get_wordnet_pos(b))) ,b) for (a,b) in corpora[1] ])

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

        n_lexems_dylan = CorpusText.count_tokens(untersuchungsbereich)
        fredDist_lem = CorpusText.pos_rank_absolut_freq(True, path_spec + "int", untersuchungsbereich, "", 'all_words',
                                                      path_property)

        # Eingelesene OANC-Datei (("Lemma", #Absolute Frequenz),"POS-Tag")
        oanc_file = FileReader.read_ANC_file(oanc_corpus, 1, 3, 2)
        # Alle Einträge aus OANC-Korpus ("lemma", #Absolute Frequenz)
        fredDist_anc = [(entry[0][0], entry[0][1]) for entry in oanc_file ]
        #print(list(fredDist_anc)[:500])
        total_anc_words = sum(val[1] for val in fredDist_anc)
        print(total_anc_words)
        difvals = CorpusText.calculate_significant_word_differences(fredDist_lem, fredDist_anc, n_lexems_dylan, total_anc_words)
        CSVwriter.write_text_differences("significant_text_differences", path_spec + "anc", True, 300, "words", difvals,
                                         'all_words', path_property)

        # ******************************************************************************************************************#

        # Signifikante Unterschiede der Worthäufigkeiten (Wortartenfilterung)
        args = [('NN', 'nouns'), ('NNP', 'proper_nouns'), ('VB', 'verbs'), ('JJ', 'adjectives')]

        for arg in args:


            # Lösungs-Ansatz : Wenn z.B. 'familiy' im OANC mehrfach auftritt, da das Wort unterschiedlich getaggt worden ist
            # .z.B als NN NNP NNS etc., dann werden alle Frequenzen von NN* aufsummiert, wenn Frequenzen abgerufen werden,
            # die der Berechnung signifikanter Nomen dienen. (Das gilt für alle Tag-Arten)
            oanc_dict = {}
            [oanc_dict.setdefault(k[0],[]).append(k[1]) for k,v in oanc_file if v.startswith(arg[0])]
            fredDist_anc = list(oanc_dict.items())
            fredDist_anc = [(values[0],sum(values[1])) for values in fredDist_anc]
            #print(fredDist_anc[:500])


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


        # ******************************************************Finde N-Gramme**********************************************#
        # *****************************************************!!!!ACHTUNG!!!!**********************************************#
        # *****************************Berechungszeit kann unter Umständen sehr lange dauern!!!*****************************#
        # Details siehe Klasse NgramFinder
        NgramFinder.find(untersuchungsbereich, path_spec + "int", path_property)


# Diese Methode normalisiert die Tokens des Dylan-Korpus
# 1. Konvertierung der Tokens zu 'lower case'
# 2. Wiederherstellung umgangsprachlich verkürzter Gerundien:
#       doin' => doing
#       lovin' => loving etc.
# => Somit kann der Lemmatizer mit den Wörtern wieder etwas anfangen
def normalize_token(token, pos_tag):
    token.lower()
    if pos_tag == 'VBG' and token.endswith('in'):
        token += 'g'
    return token

# Diese Methode bestimmt für dalle POS-Tags, wonach gefiltert werden soll,
# die richtige Wordnet-Tagbezeichnung. Das zurückgegebene Tag wird anschließend
# dem Wordnet-Lemmatizer übergeben, der so das richtige Lemma, abhängig vom POS-Tag
# ausgeben kann.
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return 'a'
    elif treebank_tag.startswith('V'):
        return 'v'
    elif treebank_tag.startswith('N'):
        return 'n'
    elif treebank_tag.startswith('R'):
        return 's'
    else:
        return 'n'

if __name__ == '__main__':
    print('This program is being run by itself')
    main()
else:
    print('I am being imported from another module')