"""
    test_atomic_weight.py

    Check the atomic_weight module. 

"""
import atomic_weight

atomic_weight_comparison_precision=0.01


def verify_atomic_weight_for_substance(formula: str, expected: float):
   
    calculated = atomic_weight.get_atomic_weight_for_compound(formula)

    assert(abs(expected - calculated) < atomic_weight_comparison_precision)


def test_for_chemical_trivial_case():
    verify_atomic_weight_for_substance("", 0.0)


def test_for_chemical_O2():
    verify_atomic_weight_for_substance("O2", 2 * 15.999)

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
    except NotImplementedError as e:
        return

    raise AssertionError("test_for_unknown_chemical() didn't fail")

