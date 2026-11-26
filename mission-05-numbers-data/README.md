# Mission 5 — Numbers and data

## 1. Task / objective
Convert values manually between decimal, binary, and hexadecimal, verify those conversions in Python, build a Python program (`number_converter.py`) that converts a user-entered decimal integer to binary and hexadecimal, and explain how text characters are stored using ASCII and UTF-8.

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
| :--- | :--- |
| Convert decimal `13` to binary. | Divide repeatedly by `2` and record remainders: `13 ÷ 2 = 6 R 1`, `6 ÷ 2 = 3 R 0`, `3 ÷ 2 = 1 R 1`, `1 ÷ 2 = 0 R 1`. Reading remainders bottom-to-top gives **`1101`**. |
| Convert decimal `25` to binary. | Divide repeatedly by `2`: `25 ÷ 2 = 12 R 1`, `12 ÷ 2 = 6 R 0`, `6 ÷ 2 = 3 R 0`, `3 ÷ 2 = 1 R 1`, `1 ÷ 2 = 0 R 1`. Reading remainders bottom-to-top gives **`11001`**. |
| Convert binary `1010` to decimal. | Multiply each bit by its power of `2`: `(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰) = 8 + 0 + 2 + 0` = **`10`**. |
| Convert binary `1101` to decimal. | `(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰) = 8 + 4 + 0 + 1` = **`13`**. |
| Convert hexadecimal `A` to decimal. | In base 16, digit `A` equals `10`, so `10 × 16⁰` = **`10`**. |
| Convert hexadecimal `1F` to decimal. | `(1 × 16¹) + (15 × 16⁰) = 16 + 15` = **`31`**. |
| Convert binary `1111` to hexadecimal. | `1111` in decimal is `8 + 4 + 2 + 1 = 15`. In hexadecimal, `15` is represented by **`F`**. |

---

### Task 5.2 — Verify using Python

| Expression tested in Python | Result | Matches manual calculation? |
| :--- | :--- | :--- |
| `bin(13)` | `'0b1101'` | Yes (`1101`) |
| `bin(25)` | `'0b11001'` | Yes (`11001`) |
| `int('1010', 2)` | `10` | Yes (`10`) |
| `int('1101', 2)` | `13` | Yes (`13`) |
| `int('A', 16)` | `10` | Yes (`10`) |
| `int('1F', 16)` | `31` | Yes (`31`) |
| `hex(31)` | `'0x1f'` | Yes (`1F`) |
| `hex(int('1111', 2))` | `'0xf'` | Yes (`F`) |

---

### Task 5.3 — Build a small number converter
Created `number_converter.py` in `mission-05-numbers-data/`. The script reads a decimal integer with `input()` and `int()`, converts it using `bin()` and `hex()`, and prints both prefixed (`0b...`, `0x...`) and unprefixed outputs.

**What `bin()` and `hex()` do:**
- `bin(n)` takes an integer `n` and returns its base-2 (binary) representation as a string prefixed with `0b`.
- `hex(n)` takes an integer `n` and returns its base-16 (hexadecimal) representation as a string prefixed with `0x`.

**Test runs from Terminal:**

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| `13` | `0b1101` (`1101`) | `0xd` (`D`) |
| `25` | `0b11001` (`11001`) | `0x19` (`19`) |
| `255` | `0b11111111` (`11111111`) | `0xff` (`FF`) |

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes (verified with Python `ord()`):**
  - Uppercase `A`: **`65`**
  - Lowercase `a`: **`97`**
- **Why a computer needs an encoding standard to store text:**
  Computers can only store and process binary numbers (`0`s and `1`s), not visual letters or symbols directly. A character-encoding standard provides an agreed mapping between each character and a specific numeric code so that different programs and computers display the same text consistently.
- **Character not part of basic ASCII:**
  The Indian Rupee symbol **`₹`** (or accented letters like `é` and emojis like `😊`) is not in basic 7-bit ASCII and requires an encoding such as **UTF-8**.

## 3. Commands / tools used
- `python3` — Ran interactive/inline conversion checks and executed `number_converter.py`.
- `input()` and `int()` — Accepted decimal input from the user and parsed it into an integer.
- `bin()` and `hex()` — Converted integers into binary (`0b...`) and hexadecimal (`0x...`) strings.
- `ord()` — Checked the ASCII decimal code points for `'A'` and `'a'`.

## 4. My understanding
All data inside a computer—numbers, text, and instructions—is stored as bits grouped into bytes. Binary (`base 2`) matches how hardware represents `0` and `1` states, hexadecimal (`base 16`) offers a compact shorthand where one hex digit maps cleanly to four bits, and character encodings like ASCII and UTF-8 map numbers back to readable text across all systems.

## 5. Difficulties faced
No major difficulties. I remembered that `bin()` and `hex()` include `0b` and `0x` prefixes, and that invalid non-numeric user input would raise a `ValueError` if not handled.

## 6. How I resolved them
Added a `try/except ValueError` block in `number_converter.py` to handle invalid input gracefully and displayed both the Python-prefixed output and the stripped digits clearly.

## 7. Evidence / files
- [number_converter.py](number_converter.py) — Working decimal-to-binary and decimal-to-hexadecimal converter.
- [README.md](README.md) — Manual steps, Python verification table, test results, and text-encoding answers.
- [../evidence/mission-05-conversions-output.txt](../evidence/mission-05-conversions-output.txt) — Saved verification and program run outputs.

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Status:** Committed on `main` and pushed to GitHub.
