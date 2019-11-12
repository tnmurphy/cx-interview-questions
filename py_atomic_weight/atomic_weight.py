import periodic_table

def get_atomic_weight_for_compound(compound: str) -> float:
    """
    This function needs to be implemented.

    Given the chemical formula of a compount return it's corresponding
    atomic weight.

    Chemical formulas are expressed in a very simple grammar.

    Element symbols always start with a capital letter, and may have
    one or two following characters which are always lowercase, for
    example:

    * "H" -> Hydrogen
    * "He" -> Helium
    * "Uuh" -> Ununhexium

    Element symbols are followed by an optional number which indicates
    how many atoms of a symbol are present in a single molecule of
    the substance.

    * "O2" -> Two atoms of oxygen
    * "H2SO4" -> Two hydrogens, One Sulphur, 4 Oxygens
    * "He" -> A single atom of Helium

    The number is omitted in the case that there is single atom
    of an element in a molecule, hence this is not valid:

    * "H2S1O4" -> Invalid because "1" is redundant here.

    """
    if not compound:
        return 0.0

    c = periodic_table.Compound(compound) 
    return c.weight()
