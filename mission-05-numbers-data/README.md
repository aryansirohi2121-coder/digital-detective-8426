# Mission 5 — Numbers and data

## 1. Task / objective
The objective of this mission is to understand data representation and digital encoding by:
- Performing manual step-by-step conversions between decimal (base 10), binary (base 2), and hexadecimal (base 16).
- Verifying the manual calculations using Python's built-in conversion functions.
- Building and executing a Python number conversion script (`number_converter.py`) that accepts user input.
- Exploring character encoding standards including ASCII and UTF-8.

---

## 2. Work completed

### Task 5.1 — Convert numbers by hand

| Question | Your working and answer |
|---|---|
| **Convert decimal 13 to binary.** | Successive division by 2:<br>13 ÷ 2 = 6, remainder 1<br>6 ÷ 2 = 3, remainder 0<br>3 ÷ 2 = 1, remainder 1<br>1 ÷ 2 = 0, remainder 1<br>Reading remainders from bottom to top: **`1101₂`** |
| **Convert decimal 25 to binary.** | Successive division by 2:<br>25 ÷ 2 = 12, remainder 1<br>12 ÷ 2 = 6, remainder 0<br>6 ÷ 2 = 3, remainder 0<br>3 ÷ 2 = 1, remainder 1<br>1 ÷ 2 = 0, remainder 1<br>Reading remainders from bottom to top: **`11001₂`** |
| **Convert binary 1010 to decimal.** | Positional expansion in powers of 2:<br>(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)<br>= (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)<br>= 8 + 0 + 2 + 0 = **`10₁₀`** |
| **Convert binary 1101 to decimal.** | Positional expansion in powers of 2:<br>(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰)<br>= (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)<br>= 8 + 4 + 0 + 1 = **`13₁₀`** |
| **Convert hexadecimal A to decimal.** | In base 16, single digits run 0–9, then A=10, B=11, C=12, D=13, E=14, F=15.<br>Digit A = (10 × 16⁰) = 10 × 1 = **`10₁₀`** |
| **Convert hexadecimal 1F to decimal.** | Positional expansion in powers of 16:<br>(1 × 16¹) + (F × 16⁰)<br>= (1 × 16) + (15 × 1)<br>= 16 + 15 = **`31₁₀`** |
| **Convert binary 1111 to hexadecimal.** | Grouping 4 bits (nibble):<br>(1 × 8) + (1 × 4) + (1 × 2) + (1 × 1) = 8 + 4 + 2 + 1 = 15₁₀<br>Decimal 15 in hexadecimal is **`F₁₆`** (or `0xF`). |

---

### Task 5.2 — Verify using Python
Tested inside the Python interactive shell:

| Operation tested | Python expression | Python output | Matches manual calculation? |
|---|---|---|---|
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes |
| Hexadecimal A to decimal | `int("A", 16)` | `10` | Yes |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` | Yes |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes |

---

### Task 5.3 — Build a small number converter
Developed `number_converter.py` using Python's built-in functions:
- `input()`: Captures string input from the terminal user.
- `int(val)`: Parses the numeric string into an integer.
- `bin(val)`: Converts an integer to a binary representation string prefixed with `0b`.
- `hex(val)`: Converts an integer to a hexadecimal representation string prefixed with `0x`.

#### Test Runs:

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| `13` | `0b1101` (1101) | `0XD` (D) |
| `42` | `0b101010` (101010) | `0X2A` (2A) |
| `255` | `0b11111111` (11111111) | `0XFF` (FF) |

---

### Task 5.4 — How is text stored?

#### 1. ASCII Decimal Codes:
- **Uppercase 'A':** Decimal `65` (Binary: `01000001`)
- **Lowercase 'a':** Decimal `97` (Binary: `01100001`)
*(Verified via Python `ord('A')` and `ord('a')`)*

#### 2. Why computers need an encoding standard to store text:
Computers exclusively store and process binary electrical signals (0s and 1s); they have no intrinsic understanding of human linguistic glyphs or letters. An encoding standard establishes a universal, unambiguous mapping between numerical binary values and visual characters so that files and messages can be accurately saved, transmitted, and read across different computer architectures and operating systems.

#### 3. Character not part of basic ASCII:
- **Example:** The Indian Rupee symbol `₹` (Unicode `U+20B9`), the Euro symbol `€` (Unicode `U+20AC`), or the emoji `😊` (Unicode `U+1F60A`). Basic ASCII only supports 7-bit characters (0–127), primarily standard English letters, digits, and basic punctuation. Characters outside this range require modern variable-width multi-byte encodings such as UTF-8.

---

## 3. Commands / tools used
- `python3`: Used to run verification expressions and execute `number_converter.py`.
- Built-in Python functions: `bin()`, `hex()`, `int()`, `ord()`, `input()`, `print()`.

---

## 4. My understanding
At the lowest physical level, all digital computers represent data using bits (0 and 1) due to two-state transistor switches. Because reading long strings of binary is difficult for humans, hexadecimal is widely used as a compact representation where each hex digit precisely represents 4 binary bits (a nibble). Furthermore, understanding character encoding reveals that text is merely numbers mapped to glyphs through standardized tables like ASCII and UTF-8.

---

## 5. Difficulties faced
No major difficulties. Noticed that Python's `bin()` and `hex()` return strings prefixed with `0b` and `0x`, so added code formatting to present both raw and prefixed versions clearly.

---

## 6. How I resolved them
Formatted the script output using slice syntax (`[2:]`) to show both the prefixed representation and the raw numeral string cleanly.

---

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`: Complete Python script for number base conversion.
- `mission-05-numbers-data/README.md`: This comprehensive report with manual calculations, verification tables, and encoding theory.

---

## 8. Commit details
- **Commit message:** `Build number converter and practise data representation`
- **Push status:** Verified and pushed to remote GitHub repository `origin/master`.
