import importlib
from input_reader import *
import sys


def main():
    persian_documents = read_xml(
        '../raw-database/Persian.xml', '{http://www.mediawiki.org/xml/export-0.10/}')
    english_documents = read_csv('../raw-database/English.csv')
    for i in range(10):
        sys.stdout.buffer.write(persian_documents[i].encode("utf-8"))
    for i in range(10):
        print(english_documents[i])


if __name__ == "__main__":
    main()
