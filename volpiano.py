from urllib.request import urlopen
from io import StringIO
from csv import DictReader
from difflib import SequenceMatcher
import re

paris15181 = "https://cantus.uwaterloo.ca/sites/default/files/csv/123631.csv"

valid_characters_re = r"[1-9a-sA-Sw-zW-Z{\[\]\-]"


def obtain(csvSource=paris15181, maxLength=10000):
    """Get a list of volpiano strings.

    Fetch a csv from the cantus database, and extract
    the first maxLength volpiano strings from it."""
    contents = urlopen(csvSource).read().decode("utf8")
    # The DictReader only reads files (not strings)
    contentsF = StringIO(contents)
    csvDict = DictReader(contentsF)
    volpianos = []
    for row in csvDict:
        v = row["volpiano"]
        if v and len(v) <= maxLength:
            volpianos.append(v)
    return volpianos


def validate(volpiano):
    """Return True if volpiano is a valid volpiano string.

    The comparison is done based on whether all characters
    in the string are valid volpiano characters.
    """
    trebleClef = "1---"
    bassClef = "2---"
    if volpiano[:4] not in [trebleClef, bassClef]:
        return False
    invalidCharacters = re.sub(valid_characters_re, "", volpiano)
    return not invalidCharacters


def compare(v1, v2):
    """Compare two volpiano strings.

    Return a similarity metric beteween [0, 1].
    """
    comp = SequenceMatcher(a=v1, b=v2)
    return comp.ratio()
