import pytest
import periodic_table
import sys
import os

sys.path.append(os.getcwd())
import data_for_test


def test_periodic_table_get():
    """Test that a single table is returned by
       multiple calls to get()"""
    table = periodic_table.PeriodicTable().get()
    table2 = periodic_table.PeriodicTable().get()
    assert table == table2


def test_oxygen():
    assert periodic_table.get_atomic_weight_for_element("O") == 15.999
    assert periodic_table.get_atomic_weight_for_element("Ar") == 39.9481


# Add more tests here!


def test_element():
    e = periodic_table.Element("O", 15.999)
    assert e.weight == 15.999
    assert e.symbol == "O"


def test_periodic_table_element_by_symbol():
    """Check that an element can be obtained by symbol"""
    table = periodic_table.PeriodicTable.get()
    e = table.element_by_symbol("O")
    assert e.weight == 15.999
    assert e.symbol == "O"


def test_periodic_table_element_by_symbol():
    """Check that a lookup of a non-element fails"""
    table = periodic_table.PeriodicTable.get()
    with pytest.raises(periodic_table.InvalidAtomicSymbol):
        e = table.element_by_symbol("X")


def test_table_count():
    """Ensure that the default table has the expected 119 elements
       Including Ununennium which is predicted but has not been observed
    """
    t = periodic_table.PeriodicTable().get()
    assert len(t) == 119


def test_table_count():
    """ Check for all the elements we expect.
    """
    t = periodic_table.PeriodicTable.get()
    for s in data_for_tests.symbols:
        assert s in PeriodicTable


def test_table_load_from_jsonfile():
    """Test loading a non-default table. Is this really important? 
    .......not very much as we don't expect chemistry to change but
    it's part of the machinery so it must be tested."""
    t = periodic_table.PeriodicTable("test_1.json")
    assert len(t) == 2
    assert t.element_by_symbol("He")
    assert t.element_by_symbol("Li")
    with pytest.raises(periodic_table.InvalidAtomicSymbol):
        e = t.element_by_symbol("O")


################### Test Compounds

# We're not testing the chemical validity of the formula
# since that requires a much more complicated set of rules
# This is a simple ruleset which in a pseudo-regexp would
# be like this:
#  ([:symbol:]([0-9]+)?)+
# There is also no claim to support brackets which would
# require a more sophisticated parser - perhaps a recursive
# descent one. Such things could be the basis of future
# enhancements.


def test_compound_create_empty():
    c = periodic_table.Compound("")
    assert c.weight() == 0.0


def test_compound_create_simple():
    c = periodic_table.Compound("O")


def test_compound_create_simple_numbered():
    c = periodic_table.Compound("O2")


def test_compound_create_simple_invalid():
    with pytest.raises(periodic_table.InvalidFormula):
        c = periodic_table.Compound("2O")


def test_compound_create_2letter1letter():
    """Use an initial 2 char symbol that 
    can be confused with a single character one."""
    c = periodic_table.Compound("CaC")


def test_compound_create_1letter1letter():
    c = periodic_table.Compound("NO")


def test_compound_create_1letter1letternumbered():
    c = periodic_table.Compound("N2O2")


def test_compound_create_3letter1letter():
    c = periodic_table.Compound("UUeO")
