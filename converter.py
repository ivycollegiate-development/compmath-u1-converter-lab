"""Unit Converter — Lab Starter.

This converter WORKS but has NO GUARDRAILS — and one quietly wrong formula.
Your job: fix the wrong math, make bad input ask again, and add conversions.
"""

MENU = """
Choose a conversion:
  1) Fahrenheit -> Celsius
  2) Celsius -> Fahrenheit
  3) Celsius -> Kelvin
  4) km -> miles
  5) miles -> km
  6) kg -> lbs
  7) lbs -> kg
  q) quit
"""

# Exact conversion factors
KM_PER_MILE = 1.609344
KG_PER_LB = 0.45359237


def get_number(prompt):
    """Ask the user for a number.

    BUG: if the user types something that is not a number,
    float() raises ValueError and the whole program crashes.
    FIX ME: wrap this in try/except so bad input asks again.
    """
    raw = input(prompt)
    return float(raw)


def f_to_c(f):
    """Convert Fahrenheit to Celsius.

    BUG: this formula is MISSING a step — it gives a quietly wrong
    answer with no crash and no error.
    FIX ME: compare it with the code-along version from today's lesson.
    """
    return f * 5 / 9


def c_to_f(c):
    """Convert Celsius to Fahrenheit (this one is correct)."""
    return c * 9 / 5 + 32


def c_to_k(c):
    """Convert Celsius to Kelvin (this one is correct)."""
    return c + 273.15


def km_to_miles(km):
    """Convert kilometers to miles (this one is correct)."""
    return km / KM_PER_MILE


def miles_to_km(mi):
    """Convert miles to kilometers (this one is correct)."""
    return mi * KM_PER_MILE


def kg_to_lbs(kg):
    """Convert kilograms to pounds (this one is correct)."""
    return kg / KG_PER_LB


def lbs_to_kg(lbs):
    """Convert pounds to kilograms (this one is correct)."""
    return lbs * KG_PER_LB


def main():
    print("=== Unit Converter v0 (no guardrails) ===")
    while True:
        print(MENU)
        choice = input("> ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Please pick 1-7, or q.")
            continue

        n = get_number("Your number: ")

        if choice == "1":
            result = f_to_c(n)
        elif choice == "2":
            result = c_to_f(n)
        elif choice == "3":
            result = c_to_k(n)
        elif choice == "4":
            result = km_to_miles(n)
        elif choice == "5":
            result = miles_to_km(n)
        elif choice == "6":
            result = kg_to_lbs(n)
        else:
            result = lbs_to_kg(n)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
