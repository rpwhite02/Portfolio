class Document:
    """
    The Document class represents the data in a single web page, or document,
    and computes the term frequency for a given term inside the given document
    or web page.
    """
    def __init__(self, path):
        """
        The initializer for the Document class takes a file path and computes
        the term frequency for each term in the document with the given file
        path in the parameter.
        """
        count = 0
        self._path = path
        self._dictionary = dict()
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                for word in line.split():
                    word = normalize_token(word)
                    count += 1
                    if word not in self._dictionary:
                        self._dictionary[word] = 1
                    else:
                        self._dictionary[word] += 1
        for word in self._dictionary:
            self._dictionary[word] = self._dictionary[word] / count

    def term_frequency(self, term):
        """
        the term_frequency function calculates the term frequency for a given
        term by searching the dictionary created in the initializer to look for
        the given term in the contents. If the term is not in the dictionary,
        return 0.
        """
        term = normalize_token(term)
        if term not in self._dictionary.keys():
            return 0
        else:
            return self._dictionary[term]

    def get_path(self):
        """
        The get_path function returns the file path for the given document
        object.
        """
        return self._path

    def get_words(self):
        """
        The get_words function returns a list of the unique, normalized words
        in the given document object.
        """
        self._li = []
        for key in self._dictionary:
            if key not in self._li:
                self._li.append(key)
        return self._li
