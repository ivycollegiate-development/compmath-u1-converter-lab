
---

## Before you start — every session

You work on the class VS Code server, in your own clone of this repo.
Your userid shows up in your repo name, your clone URL, and your filenames
via `$(whoami)`: `whoami` prints your userid, and `$(whoami)` inserts it
automatically. If the folder is missing, re-clone it — your lesson has the
exact URL, always ending in `_student.git`.

**Run this first, every session** — it checks you are in the right folder,
then clones your repo if you don't have it yet:

```bash
cd ~
git clone https://github.com/ivycollegiate-development/compmath-u1-converter-lab-$(whoami)_student.git
cd compmath-u1-converter-lab-$(whoami)_student
bash setup.sh
```

The script stops with `[STOP]` if you are not in your home directory,
because cloning into the wrong folder scatters your work where you can't
find it. Fix that with `cd ~` and run it again.

- It prints your clone URL before cloning — check it ends in `_student.git`.
- It says `[OK] Verified: <your-repo>` when you are in the right place.
- Already cloned? It runs `git pull` instead, to get changes I pushed.

**Pull before work, every session** — it gets any changes I pushed to your
repo since last class:

```bash
cd ~/<your-clone-folder>
git config pull.rebase false
git pull
```

- `git config pull.rebase false` tells git how to combine work; run it once,
  it is not an error if you already ran it.
- If the pull prints `Already up to date.` you have everything.
- **Asked for a username/password?** GitHub username plus Personal Access
  Token (PAT) — never your GitHub password.

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
