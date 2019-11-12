import json
import os


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
        self.elements = set()
        self.filename = filename
        self._load_from_jsonfile(filename)

    def _load_from_jsonfile(self, filename: str):
        """Load a periodic table from a json format file"""
        with open(filename) as jf:
            j = json.load(jf)
            for je in j["elements"]:
                e = Element(je["symbol"], je["atomic_mass"])
                self.elements.add(e)

    @classmethod
    def get(cls, filename=DEFAULT_JSON):
        """ Get an existing instance if there is one or create it """
        if cls.instance == None:
            cls.instance = cls(filename)
        return cls.instance

    def element_by_symbol(self, symbol: str) -> Element:
        for e in self.elements:
            if symbol == e.symbol:
                return e
        raise InvalidAtomicSymbol("Symbol {} not found".format(symbol))

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, symbol: str):
        """Make periodic table behave like partially like a dictionary"""
        return self.elements[key]


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
    element = t.element_by_symbol(element_symbol)
    return element.weight
