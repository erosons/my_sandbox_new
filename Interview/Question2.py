import logging


words1 = ['dog', 'kitten']
words2 = ['tiger', 'god']


def anagram_pair_exists(words1, words2):
    """
    anagram_pair_exists(words1, words2) does comparism 
     of two list checking for anagrams

    Parameters:
    words1 : first list
    words2 : second list
    """
    try:

        for wd in words1:
            for wd1 in words2:
                if sorted(wd) == sorted(wd1):
                    print("True as {} and {} are anagrams".format(wd, wd1))
                else:
                    print(" False  as {} and {} are not anagrams".format(wd, wd1))
    except:
        logging.info('Parameters not supplied')


anagram_pair_exists(words1, words2)