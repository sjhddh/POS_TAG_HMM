__author__ = 'AaronSun'

from sklearn.cross_validation import KFold
from Calculation import Calculation
from Test import Test
import time


# idea here:
# divide all the files base on sentence.
# index them
# generate a random index set
# with 90%/10% choose from random index set
# choose them by
# then, when manipulate with sentence, do further processing
class CrossValidation:
    def __init__(self, trains, targets):
        self.trains = trains
        self.targets = targets
        self.size = len(trains)

    # method for doing Cross Validation.
    def do_cv(self):
        # use imported sklearn library to generate
        # 10 section of random indexes for all the corpus
        kf = KFold(self.size, n_folds=10)
        # reset accuracy
        accuracy = 0
        round = 0
        # do for all the 10 set of corpus
        for train_index, test_index in kf:
            round += 1
            train_word = []
            train_tag = []
            test_word = []
            test_tag = []
            # formalize them into training set
            for i in train_index:
                train_word.append(self.trains[i])
                train_tag.append(self.targets[i])
            # formalize them into test set
            for i in test_index:
                test_word.append(self.trains[i])
                test_tag.append(self.targets[i])

            # do calculation
            print('start counting and calculating: ' + time.strftime("%H: %M: %S"))
            c = Calculation(train_word, train_tag)
            c.calculateProbability()
            # run test for test sets
            print 'start running viterbi on', len(test_word), 'tests: ' + time.strftime("%H: %M: %S")
            t = Test(c.count_i, c.count_w, c.p_ji, c.p_wk, test_word, test_tag)
            a = t.do_cv_test()
            print round, '/ 10 CV accuracy: ', a
            accuracy += a
        # output the mean accuracy
        return accuracy / 10




