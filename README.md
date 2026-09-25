# Unit Converter — Lab Starter (Unit 1)

## Before you start — clone YOUR repo (not this one)

You received your OWN copy of this repo by accepting a GitHub invitation in
your email. Its name ends in `_student` — that is the one you work in.

On the class VS Code server, clone it once:

```bash
git clone https://github.com/ivycollegiative-development/compmath-u1-converter-lab-$(whoami)_student.git
cd compmath-u1-converter-lab-$(whoami)_student
```

Wait — check the URL carefully: the org is `ivycollegiate-development`.
The exact URL for YOUR repo is in the lesson sheet and the Classroom
assignment. `$(whoami)` prints your userid and inserts it automatically.

Then pull before work, every session:

```bash
git config pull.rebase false
git pull
```

- `git pull` gets any changes pushed to your repo since last class.
- **Asked for a username/password?** GitHub username plus Personal Access
  Token (PAT) — never your GitHub password.

---

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

## How to hand this in (git push — no screenshots)

1. Commit your fixed `converter.py` with a real message:

   ```bash
   git add converter.py
   git commit -m "Fix f_to_c formula and add bad-input guardrail"
   ```

2. Push to **your own repo** (this one):

   ```bash
   git push origin main
   ```

3. Confirm all 5 tests pass:

   ```bash
   python3 test_converter.py
   ```

4. In Google Classroom, submit a link to your repo
   (`https://github.com/ivycollegiate-development/<your-repo-name>`).

Your commit IS your submission. The tests are the rubric — 5/5 passing is
the goal. Do **not** submit screenshots; we grade the pushed code.