# Unit Converter — Lab Starter (Unit 1)

Your job today: turn this broken converter into a correct, safe one.

## What's here

- `converter.py` — a converter with **no guardrails** and **one quietly wrong
  formula**. It crashes on bad input and answers °F → °C wrong without complaining.
- `test_converter.py` — checks your converter's behavior. Run it to see how you're doing.
- `README.md` — this file.

## Your job

Run the converter first and see it fail **two different ways**:

```bash
python3 converter.py
```

- Pick **Fahrenheit -> Celsius**, enter 212 → it says **122.0**. Wrong. 212 °F
  is 100 °C. No crash — just a quietly wrong answer.
- Then type `hello` when it asks for a number. Watch it crash.

Then check yourself:

```bash
python3 test_converter.py
```

Fix the two `FIX ME` bugs in `converter.py`, add the remaining conversions with
your partner, and re-run the tests until **5/5 passing**.
