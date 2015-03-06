Hello world

This is basically a project about NLP POS tagging.
If you do not understand what is the meaning of the short forms above, then you are definitely not interested here.

The general structure is:
1. main: control over all intereactions
2. ReadIN: read in the corpus file for learning
3. Calculation: by bayes' rules, we need to count the appearence of all the words in corpus and work out particular probability. Wiki for details
4. Test: running the test fro tagging on new sentences
5. Viterbi: the algorithm used in testing
6. CrossValidaiton: Validate the accuracy