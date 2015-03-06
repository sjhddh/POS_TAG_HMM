from __future__ import division

__author__ = 'AaronSun'

import json


class Calculation:
    def __init__(self, trains, targets):
        # with the same name as indicated in Lecture notes
        self.count_ij = {}
        self.count_i = {}
        self.count_wk = {}
        self.count_w = {}
        self.count_k = {}    # count for all words
        self.p_ji = {}      # probabilities
        self.p_wk = {}
        self.test = []       # For storing the test sentence
        self.trains = trains
        self.targets = targets

    # count with two dimension keys
    def do2DCount(self, count, key1, key2):
        # if the key not exist, then init as count 1
        try:
            count[(key1, key2)] += 1
        except KeyError:
            count[(key1, key2)] = 1

    # count with one dimension key
    def do1DCount(self, count, key):
        # if the key not exist, then init as count 1
        try:
            count[key] += 1
        except KeyError:
            count[key] = 1

    # the general process for counting the words and tags
    def do_count(self):
        # main method for manipulating data
        # i for each sentence
        # j for each word in sentence
        for i in range(len(self.trains)):
            for j in range(len(self.trains[i])):
                # in case of index error
                try:
                    self.do2DCount(self.count_ij, self.targets[i][j], self.targets[i][j+1])
                except IndexError:
                    pass
                self.do1DCount(self.count_i, self.targets[i][j])
                self.do2DCount(self.count_wk, self.trains[i][j], self.targets[i][j])
                self.do1DCount(self.count_w, self.trains[i][j])

    def calculateProbability(self):
        self.do_count()

        # assume the words only go for their possible tags
        for key_wk in self.count_wk:
            # if key_wk[1] in self.count_i:
            try:
                self.p_wk[key_wk] = self.count_wk[key_wk] / self.count_i[key_wk[1]]  # + len(self.count_i)
            # add one smooth
            except KeyError:
                print('This will never happen')
                self.p_wk[key_wk] = 1 / len(self.count_i)

        for i in self.count_i:
            for j in self.count_i:
                # if (i, j) in self.count_ij:
                try:
                    self.p_ji[(j, i)] = (1 + self.count_ij[(i, j)]) / (self.count_i[i] + len(self.count_i))
                except KeyError:
                    self.p_ji[(j, i)] = 1 / len(self.count_i)

