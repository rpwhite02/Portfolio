import re


def normalize_token(token: str):
    """
    Returns a "normalized" version of the given token (str). A normalized
    token is one where all letters are converted to lowercase and all
    non-letters (e.g., punctuation) are removed.
    """
    return re.sub(r'\W+', '', token.lower())
  
