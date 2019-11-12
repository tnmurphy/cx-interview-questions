import json
import os
import re


class InvalidAtomicSymbol(KeyError):
    """
    Raised when an invalid atomic symbol is looked up.
    """


class Element(object):
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight

    def __hash__(self):
        return hash(self.symbol)


class PeriodicTable(object):
    """Represent a table, load it up, create elements etc."""

    DEFAULT_JSON = os.path.join(os.path.dirname(__file__), "periodic_table.json")
    instance = None

    def __init__(self, filename=DEFAULT_JSON):
        super(PeriodicTable, self)
        self.elements = {}
        self.filename = filename
        self._load_from_jsonfile(filename)

    def _load_from_jsonfile(self, filename: str):
        """Load a periodic table from a json format file"""
        with open(filename) as jf:
            j = json.load(jf)
            for je in j["elements"]:
                e = Element(je["symbol"], je["atomic_mass"])
                self.elements[e.symbol] = e

    @classmethod
    def get(cls, filename=DEFAULT_JSON):
        """ Get an existing instance if there is one or create it """
        if cls.instance == None:
            cls.instance = cls(filename)
        return cls.instance

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, key):
        """Make periodic table behave partially like a dictionary with the element symbol as the key"""
        try:
            e = self.elements[key]
        except KeyError as k:
            raise InvalidAtomicSymbol("Symbol {} not found".format(key))
        return e

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, key):
        return key in self.elements


class InvalidFormula(Exception):
    pass


class Compound(object):
    """The Compound class needs Element and PeriodicTable to exist.
       Initially it is not sophisticated enough to represent formulae
       which require brackets. It also makes no attempt to ensure that
       elements are listed according to convention.

       This simplicity allows the use of a regular expression to parse
       formula strings.  It should offer relatively good performance since
       it will construct some kind of minimal finite automaton. To parse
       chemical formulas more truely would require more sophistication
       as to the conventional ordering of elements and recursion and the
       question of whether a compound is "possible" or not.

       A Regular experssion might be simple and efficient to execute but
       in all likelihood the data structures that it creates in the match
       object could end up making it use a lot of memory and be slow.
       A better approach might be to simply test via dictionary lookup for 
       the 3-letter, the 2-letter and then 1-letter symbols and progress
       through the string that way.
    """

    periodic_table = PeriodicTable.get()
    symbol_multi_pattern = "|".join(
        [k for k in periodic_table.elements.keys() if len(k) > 1]
    )
    symbol1_pattern = (
        "[" + "".join([k for k in periodic_table.elements.keys() if len(k) == 1]) + "]"
    )
    formula_pattern = "(" + symbol_multi_pattern + "|" + symbol1_pattern + ")([0-9]+)?"
    formula_re = re.compile(formula_pattern)

    def __init__(self, formula: str):
        self.element_counts = Compound.parse_formula_to_tuples(formula)

    @classmethod
    def parse_formula_to_tuples(cls, formula: str) -> list:
        """This method uses a regexp and finditer to look for elements
        and their counts. It checks that they are contiguous."""
        element_counts = []

        if formula == "":
            return []

        index = 0
        old_match_end = 0  # used to check that the matches are contiguous
        for m in cls.formula_re.finditer(formula):
            print(m.groups())
            match_start, match_end = m.span()
            if match_start != old_match_end:
                raise InvalidFormula(
                    "Formula contains non-symbols: '{}'".format(
                        formula[old_match_end:match_start]
                    )
                )
            old_match_end = match_end
            if m.groups()[-1] == "1":
                raise InvalidFormula(
                    "Invalid Element count of 1 for element {}".format(index)
                )
            if m.groups()[-1] == None:
                count = 1
            else:
                count = int(m.groups()[-1])

            element = cls.periodic_table[m.groups()[-2]]
            element_counts.append((element, count))

        return element_counts

    def weight(self):
        """Add up the weights of all the elements"""
        try:
            return self._weight
        except AttributeError as e:
            pass

        self._weight = 0.0
        for e, count in self.element_counts:
            self._weight += e.weight * count

        return self._weight


def get_atomic_weight_for_element(element_symbol: str) -> float:
    """
    This function needs to be implemented.

    Given an element's atomic symbol such as "O", "He" or "Ti" return the
    element's corresponding atomic weight as a floating point number.

    If an atomic symbol which does not exist is requested, then
    raise a InvalidAtomicSymbol exception.

    All the data you need to implement this function is in periodic_table.json.

    This function can look up data in that file, or alternativly you can
    extract the relevant data and build a structure here. Whichever
    approach you take, please include any code you used to do this.
    """
    t = PeriodicTable.get()
    element = t[element_symbol]
    return element.weight
