import pytest
import periodic_table


def test_periodic_table_get():
    table = periodic_table.PeriodicTable().get()
    table2 = periodic_table.PeriodicTable().get()
    assert table == table2


def test_oxygen():
    assert periodic_table.get_atomic_weight_for_element("O") == 15.999


# Add more tests here!


def test_element():
    e = periodic_table.Element("O", 15.999)
    assert e.weight == 15.999
    assert e.symbol == "O"


def test_periodic_table_element_by_symbol():
    table = periodic_table.PeriodicTable().get()
    e = table.element_by_symbol("O")
    assert e.weight == 15.999
    assert e.symbol == "O"


def test_periodic_table_element_by_symbol():
    table = periodic_table.PeriodicTable().get()
    with pytest.raises(periodic_table.InvalidAtomicSymbol):
        e = table.element_by_symbol("X")


# def test_table_count():
#    t = periodic_table.PeriodicTable()
#    assert len(t) == 238
