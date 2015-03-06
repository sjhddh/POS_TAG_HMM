__author__ = 'AaronSun'
# the overall process of this project
# 1. ReadIN: read all the files and formalise them into arrays of trains and targets
# 2. CrossValidation: 10-fold validation to changing trains and targets
# 3. Calculation: calculating the counts and output probabilities
# 4. Test: Conducting the test process
# 4. ViterbiAlg: find the best result by Vterbi Algorithm

from ReadIN import ReadIN
from Calculation import Calculation
from Test import Test
from CrossValidation import CrossValidation
import time


def main():
    # instruction for choosing tagging service
    np = raw_input('choose: 1. cross validation test; 2. simple test : ')
    # if is not a int value, return wrong
    try:
        cmd = int(np)
    except ValueError:
        print('invalid cmd')

    # if is CV
    if cmd == 1:
        print('start loading all files: ' + time.strftime("%H: %M: %S"))
        r = ReadIN()
        trains, targets = r.formalizeSentences(r.formalizeDataset(r.readFile()))
        cv = CrossValidation(trains, targets)
        print('start doing cross validation: ' + time.strftime("%H: %M: %S"))
        mean = cv.do_cv()
        print 'mean CV accuracy: ', mean

    # if is simple sentence test
    else:
        sentence = raw_input('input your sentence: ')
        s_array = sentence.split()
        print('start loading all files: ' + time.strftime("%H: %M: %S"))
        r = ReadIN()
        trains, targets = r.formalizeSentences(r.formalizeDataset(r.readFile()))
        print('start counting and calculating: ' + time.strftime("%H: %M: %S"))
        c = Calculation(trains, targets)
        c.calculateProbability()
        print('start running viterbi: ' + time.strftime("%H: %M: %S"))
        t = Test(c.count_i, c.count_w, c.p_ji, c.p_wk, s_array, [])
        t.do_simple_test()


if __name__ == '__main__':
    main()