from __future__ import division

__author__ = 'AaronSun'

from ViterbiAlg import viterbiAlg

# a class for testing new data
# 1.
class Test:
    # tags: a array of all the tags in training set
    def __init__(self, tags_count, words, p_ji, p_wk, test_word, test_tag):
        self.tags = tags_count
        self.words = words # is a dic of all words
        self.p_ji = p_ji
        self.p_wk = p_wk
        self.test_word = test_word
        self.test_tag = test_tag

    # in case the input sentence is not well formed
    def formaliseSentences(self):
        pass

    # doing check, whether t1 and t2 are equal
    def match(self, t1, t2):
        for i in range(len(t1)):
            if t1[i] != t2[i]:
                return False
        return True

    def do_cv_test(self):
        accuracy = 0
        # run viterbi to get the predicted result
        for i in range(len(self.test_word)):
            match_count = 0
            v = viterbiAlg(self.test_word[i], self.tags, self.words, self.p_ji, self.p_wk)
            result = v.runViterbi()
            # check whether the tags will match
            for n in range(len(result)):
                if result[n] == self.test_tag[i][n]:
                    match_count += 1
            # the accuracy in every sentence
            accuracy += match_count / len(self.test_tag[i])
        # return the accuracy of all sentences
        return accuracy / len(self.test_word)

    def do_simple_test(self):
        # simply put the test sentence into Viterbi
        v = viterbiAlg(self.test_word, self.tags, self.words, self.p_ji, self.p_wk)
        result = v.runViterbi()
        print(self.test_word)
        print(result)
