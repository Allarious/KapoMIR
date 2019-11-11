import importlib
from input_reader import *
from preprocess import *
import sys


def main():
    persian_documents = read_xml(
        '../raw-database/Persian.xml', '{http://www.mediawiki.org/xml/export-0.10/}')
    english_documents = read_csv('../raw-database/English.csv')
    for i in range(10):
        persian_preprocess(persian_documents[i])
    for i in range(10):
        #feed in the body of documents index 1
        english_preprocess(english_documents[i][1])


if __name__ == "__main__":
    main()
