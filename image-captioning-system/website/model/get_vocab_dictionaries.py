import os
from django.conf import settings


def read_word_dictionary(word_dictionary_file_path):
    """
    Read word dictionary takes a file input and assumes each line is of the following format: "word,id".
    It then converts this into a dictionary and returns
    :param word_dictionary_file_path: File path of word_dictionary file
    :return: Dictionary of words and associated ids
    """
    word_dict = dict()
    with open(word_dictionary_file_path) as f:
        for line in f:
            words = line.strip().split(",")
            word_dict[words[0]] = int(words[1])

    return word_dict


def read_id_to_word_dictionary(word_dictionary_file_path):
    """
    Read id to word dictionary takes a file input and assumes each line is of the following format: "word:id".
    It then converts this into a dictionary where key is the id and value is the word.
    :param word_dictionary_file_path: File path of word_dictionary file
    :return: Dictionary of id and associated words
    """
    word_dict = dict()
    with open(word_dictionary_file_path) as f:
        for line in f:
            words = line.strip().split(",")
            word_dict[int(words[1])] = words[0]

    return word_dict


def get_word_dictionary():
    return read_word_dictionary(os.path.join(settings.BASE_DIR, 'model/model_data/word_dictionary.txt'))


def get_id_dictionary():
    return read_id_to_word_dictionary(os.path.join(settings.BASE_DIR, 'model/model_data/word_dictionary.txt'))
