from __future__ import division

__author__ = 'AaronSun'

import time


class viterbiAlg:
    # w is an array of words in test sentence,
    # t is the list count of all tags
    # wordslib contains all learned words
    # v is the number of all words
    # n is the number of total number of words,
    # k is the total number of tags
    def __init__(self, w, t, v, p_ji, p_wk):
        self.w = w
        self.t_count = t
        self.t = t.keys()
        self.wordslib = v   # a lib dic
        self.v = len(v)
        self.n = len(w)
        self.k = len(t)
        self.score = {}
        self.backpointer = {}
        self.p_ji = p_ji
        self.p_wk = p_wk
        self.output_tag = []
        for i in range(self.n):
            self.output_tag.append(0)

    # add-one-smooth for unknown words
    def deal_unknown(self, word):
        for i in self.t:
            self.p_wk[(word, i)] = 1  # / self.t_count[i]
        self.wordslib[word] = 1

    def initialise(self):
        for i in range(self.k):
            # if the world is not appreared
            # if self.w[0] not in self.wordslib:
            try:
                current_word = self.wordslib[self.w[0]]
            except KeyError:
                self.deal_unknown(self.w[0])
            # if (self.w[0], self.t[i]) in self.p_wk:
            try:
                self.score[(i, 0)] = self.p_wk[(self.w[0], self.t[i])] * self.p_ji[(self.t[i], '*')]
            except KeyError:
                pass

    def induction(self):
        for j in range(1, self.n):
            for i in range(self.k):
                max_score = float(0)
                max_backpointer = 0
                # if self.w[j] not in self.wordslib:
                try:
                    current_word = self.wordslib[self.w[j]]
                except KeyError:
                    self.deal_unknown(self.w[j])

                # if (self.w[j], self.t[i]) in self.p_wk:
                try:
                    current_p_wk = self.p_wk[(self.w[j], self.t[i])]
                    for k in range(self.k):
                        # if (k, j - 1) in self.score:
                        try:
                            c = float(self.score[(k, j - 1)] * self.p_ji[(self.t[i], self.t[k])] * self.p_wk[(self.w[j], self.t[i])])
                            if max_score < c:
                                max_score = c
                                max_backpointer = k
                        except KeyError:
                            pass

                    self.score[(i, j)] = max_score
                    self.backpointer[(i, j)] = max_backpointer
                except KeyError:
                    pass

    def backtracing(self):
        max_n = 0
        pointer = 0
        for i in range(self.k):
            # if (i, self.n - 1) in self.score:
            try:
                if max_n < self.score[(i, self.n - 1)]:
                    max_n = self.score[(i, self.n - 1)]
                    pointer = i
            except KeyError:
                pass
        self.output_tag[self.n - 1] = pointer

        for i in reversed(range(self.n - 1)):
            # if (self.output_tag[i + 1], i + 1) in self.backpointer:
            try:
                self.output_tag[i] = self.backpointer[(self.output_tag[i + 1], i + 1)]
            except KeyError:
                pass

    # a method for mapping the output best tagging to POS tags
    # bestTagging are the array of best tags in sentence
    # T are all the tags
    def getTagged(self, bestTagging, t):
        POS = []
        for i in bestTagging:
            POS.append(t[i])
        return POS

    def runViterbi(self):
        self.initialise()
        self.induction()
        self.backtracing()
        return self.getTagged(self.output_tag, self.t)


