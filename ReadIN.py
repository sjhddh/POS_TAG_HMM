__author__ = 'AaronSun'

import os


class ReadIN:
    def __init__(self):
        self.trains = [[]]
        self.targets = [[]]

    def readFile(self):

        # this is the part to read all the files
        path = 'WSJ-2-12'
        dataset = ' */* '
        for sub_entry in os.listdir(path):
            entry_path = os.path.join(path, sub_entry)
            if os.path.isdir(entry_path):
                for file_name in os.listdir(entry_path):
                    file_entry = os.path.join(entry_path, file_name)
                    if os.path.isfile(file_entry):
                        file = open(file_entry)
                        dataset += file.read()
        return dataset

    def formalizeDataset(self, d):
        # rule out meaning less symbols here, and split the sentence by sentence
        # here is a notion '\/' which is always a mess msg. I regart it a & symbol
        sentences = d.replace('[ ', '').replace(' ]', '').replace('=', '').replace('. \n\n', '. */* <split_point> */* ')\
            .replace('\/', '&').split('<split_point>')

        return sentences

    def formalizeSentences(self, s):
        try:
            for each in s:
                trains = []
                targets = []
                word = each.split()
                for i in word:
                    # store every single words in 2-d
                    # even though we ruled out some messy '\/'
                    # there is still some mess msg like Chiat\/NNP in file 0869, which cannot change to &
                    # so just catch the error here.

                    trains.append(i.split('/')[0])
                    targets.append(i.split('/')[1])

                # in 1-d, store sentence by sentence
                self.trains.append(trains)
                self.targets.append(targets)
        except IndexError:
            pass

        # after everything, delete the first item, which is an empty []
        del self.targets[0]
        del self.trains[0]

        return self.trains, self.targets

