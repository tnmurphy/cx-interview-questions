"""
    test_atomic_weight.py

    Check the atomic_weight module. 

"""
import atomic_weight
import periodic_table

atomic_weight_comparison_precision = 0.0001


def verify_atomic_weight_for_substance(formula: str, expected: float):

    calculated = atomic_weight.get_atomic_weight_for_compound(formula)

    assert abs(expected - calculated) < atomic_weight_comparison_precision


def test_for_chemical_trivial_case():
    verify_atomic_weight_for_substance("", 0.0)


def test_for_chemical_O2():
    verify_atomic_weight_for_substance("O2", 2 * 15.999)


def test_for_arbitrarily_complicated_substance():
    """Not a real substance though"""
    verify_atomic_weight_for_substance("Al4O2H2", 141.94015428)


def test_compound_weight_multi():
    verify_atomic_weight_for_substance("N2O2", 15.999 * 2 + 14.007 * 2)


def test_compound_weight_multi_2letter():
    verify_atomic_weight_for_substance("Al4O2", 15.999 * 2 + 26.98153857 * 4)


# Add more tests here.


def test_that_test_can_fail():
    """Make sure the method does actually fail"""
    try:
        verify_atomic_weight_for_substance("O2", 1.0)
    except AssertionError as e:
        return

    raise AssertionError("test_that_test_can_fail() didn't fail")


def test_for_unknown_chemical():
    """Make sure the method fails for an unknown substance"""
    try:
        verify_atomic_weight_for_substance(",.!", 1.0)
    except periodic_table.InvalidFormula as e:
        return

    raise AssertionError("test_for_unknown_chemical() didn't fail")
