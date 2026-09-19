"""Self-check tests for the Unit Converter lab.

Run:  python3 test_converter.py
Each PASS is a guardrail or correct formula working.
"""

import io
import sys
from contextlib import redirect_stdout

import converter


def run_conv(inputs):
    """Run converter.main() with scripted stdin, return captured output."""
    out = io.StringIO()
    old_stdin = sys.stdin
    sys.stdin = io.StringIO("\n".join(inputs) + "\n")
    try:
        with redirect_stdout(out):
            converter.main()
    except SystemExit:
        pass
    finally:
        sys.stdin = old_stdin
    return out.getvalue()


results = []


def check(name, fn):
    try:
        ok = fn()
        results.append((name, bool(ok), ""))
    except Exception as e:
        results.append((name, False, f"{type(e).__name__}: {e}"))


# Test 1: the Fahrenheit->Celsius formula is actually correct
def t1():
    assert abs(converter.f_to_c(212) - 100.0) < 1e-9, f"f_to_c(212) = {converter.f_to_c(212)}"
    assert abs(converter.f_to_c(32) - 0.0) < 1e-9, f"f_to_c(32) = {converter.f_to_c(32)}"
    assert abs(converter.f_to_c(-40) + 40.0) < 1e-9, f"f_to_c(-40) = {converter.f_to_c(-40)}"
    return True


# Test 2: bad input asks again instead of crashing
def t2():
    out = run_conv(["1", "hello", "212", "q"])
    return "Result" in out


# Test 3: Celsius -> Kelvin works
def t3():
    assert abs(converter.c_to_k(0) - 273.15) < 1e-9
    assert abs(converter.c_to_k(100) - 373.15) < 1e-9
    return True


# Test 4: distance and weight conversions use the exact factors
def t4():
    assert abs(converter.km_to_miles(1.609344) - 1.0) < 1e-9
    assert abs(converter.miles_to_km(1) - 1.609344) < 1e-9
    assert abs(converter.kg_to_lbs(0.45359237) - 1.0) < 1e-9
    assert abs(converter.lbs_to_kg(1) - 0.45359237) < 1e-9
    return True


# Test 5: quit works cleanly
def t5():
    out = run_conv(["q"])
    return "Goodbye" in out


check("1. F->C formula correct (212F = 100C)", t1)
check("2. bad input asks again, no crash", t2)
check("3. C->K works", t3)
check("4. km/miles + kg/lbs exact factors", t4)
check("5. quit works", t5)

print()
print("=== Self-check results ===")
passed = 0
for name, ok, err in results:
    mark = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    print(f"[{mark}] {name}" + (f"  ({err})" if err else ""))
print(f"{passed}/{len(results)} passing")
