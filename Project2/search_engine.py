import os
from document import Document
import math
from operator import itemgetter
from utils import normalize_token


class SearchEngine:
    """
    The SearchEngine class represents a directory of documents, and calculates
    the tf-idf statistic between an individual document and a given search
    term.
    """
    def __init__(self, path):
        """
        The initializer of the SearchEngine class creates an inverted index in
        the form of a dictionary, associating each term in the directory to a
        list of documents that contain that term.
        """
        self._path = path
        self._doc_objects = []
        self._dictionary = dict()
        for filename in os.listdir(path):
            self._doc_objects.append(Document(os.path.join(path, filename)))
        for doc in self._doc_objects:
            words = doc.get_words()
            for word in words:
                if word not in self._dictionary:
                    self._dictionary[word] = [doc]
                else:
                    self._dictionary[word].append(doc)

    def _calculate_idf(self, term):
        """
        The _calculate_idf function calculates the IDF for an individual term
        in a search query, and is then implemented in the search function. If
        the given term is not in the inverted index, return 0.
        """
        if term not in self._dictionary.keys():
            return 0
        else:
            denominator = self._dictionary[term]
        divis = len(self._doc_objects) / len(denominator)
        result = math.log(divis)
        return result

    def search(self, query):
        """
        The search function takes a search query as a string and returns a list
        of document paths that contain that term or string of terms sorted in
        descending order based on the tf-idf scores. If there are no documents
        with the query, return an empty list.
        """
        relevant_docs = []
        scores_and_docs = []
        for query_word in query.split():
            query_word = normalize_token(query_word)
            if query_word in self._dictionary.keys():
                for doc in self._dictionary[query_word]:
                    if doc not in relevant_docs:
                        relevant_docs.append(doc)
        if len(relevant_docs) == 0:
            return relevant_docs
        for doc in relevant_docs:
            total = 0
            for query_word in query.split():
                tf = doc.term_frequency(query_word)
                idf = self._calculate_idf(query_word)
                total += tf * idf
            scores_docs = (total, doc.get_path())
            scores_and_docs.append(scores_docs)
        sorted_list_of_tuples = sorted(scores_and_docs, key=itemgetter(0),
                                       reverse=True)
        result = []
        for pair in sorted_list_of_tuples:
            result.append(pair[1])
        return result
