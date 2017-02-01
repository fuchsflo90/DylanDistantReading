__author__ = 'Colin Sippl'

class SpeechObject(object):
    def __init__(self):
        self.quotesList = []

    def add_quote(self, sentence):
        self.quotesList.append(sentence)

    def add_pos_quote(self, index, POS_sentence):
        self.quotesList[index].change_pos_sentence(POS_sentence)

    def get_element(self, id):
        return self.quotesList[id]

    def return_all_quotes(self):
        return self.quotesList

    class Quote(object):
        def __init__(self):
            self.hasNgrams = False
            self.ngrams = []
            self.bawlrentries = []
            self.cssClasses = ""
            self.sentence = ""
            self.POS_sentence = ""
            self.ngramstring = ""

        def add_ngram(self, nGram):
            if  self.hasNgrams == False:
                self.hasNgrams = True
            self.ngrams.append(nGram)

        def return_ngram_list(self):
            return self.ngrams

        def return_sentence(self):
            return self.sentence

        def change_sentence(self, sentence):
            self.sentence = sentence

        def change_pos_sentence(self, POS_sentence):
            self.POS_sentence = POS_sentence

        def set_css_classes(self, classes):
            self.cssClasses = self.cssClasses + classes + " "

        def get_css_classes(self):
            return self.cssClasses

        def set_ngram_string(self, ngramstring):
            self.ngramstring = ngramstring

        def update_ngram_status(self, status):
            self.hasNgrams = status
