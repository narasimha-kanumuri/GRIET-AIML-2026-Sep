# DAY 1 · STEP 5 — NumPy
## Teacher Explanation Reference (every method, variable, parameter)

**Use:** keep open on second screen while teaching. Left column = general meaning, right column = what it does *in this code*.
**Spine sentence (repeat 4+ times today):** *NumPy = Fast Math Engine. One instruction. Many numbers.*

---

## 0. Two vocabulary words students confuse all day

| Word | ELI5 | Test to tell them apart |
|---|---|---|
| **Function** | A tool that stands alone. You hand it something. | Written as `name(thing)` → `len(x)`, `print(x)`, `int(x)` |
| **Method** | A tool that *belongs to* an object. The object already knows how. | Written as `thing.name()` → `instagram.sum()` |
| **Parameter / Argument** | The thing you hand in, inside the brackets. | Whatever sits between `(` and `)` |
| **Variable** | A name tag stuck on a value so you can call it later. | `total = ...` — left side is the name tag |
| **Attribute** | A *fact about* an object. No brackets. | `mixed.dtype` — no `()`, because you are asking, not doing |

> **Say out loud:** "Brackets mean *do something*. No brackets means *tell me something*."
> That one line kills the `.dtype()` vs `.dtype` error before it happens.

---

## 1. IMPORTS

```python
import csv
import numpy as np
```

| Item | In general | In this code |
|---|---|---|
| `import` | Loads a toolbox that is not switched on by default. Python ships with batteries, but not unpacked. | Switches on CSV reading and NumPy maths |
| `csv` | Standard-library module for reading/writing comma-separated files | Reads `digital_behaviour.csv` |
| `numpy` | Third-party library for fast numeric arrays | The whole point of Step 5 |
| `as np` | **Alias.** A nickname for the module. | Lets you type `np.array` instead of `numpy.array`. `np` is a worldwide convention — every book, every StackOverflow answer uses it. Do not invent your own. |

**Ask the class:** "Why not just `import numpy`?" → It works. `as np` is about typing 4,000 fewer characters over a career.

---

## 2. LOADING THE STUDENT'S OWN DATA

```python
instagram_list = []
study_list = []
```

| Item | In general | In this code |
|---|---|---|
| `[]` | An **empty list** — an ordered container that grows | Two empty buckets waiting to be filled, one per column |
| `instagram_list`, `study_list` | Variable names | Named `_list` *deliberately* so the contrast with the NumPy version later is visible on screen |

> **Teaching note:** the `_list` suffix is not decoration. In Part A they become `instagram` and `study`. The rename is the lesson.

---

```python
with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
```

| Item | In general | In this code |
|---|---|---|
| `open()` | Built-in function that connects Python to a file on disk | Opens the student's own CSV |
| `"digital_behaviour.csv"` | **1st parameter — filename/path.** A string. | The file sitting in the same folder as the script |
| `"r"` | **2nd parameter — mode.** `r` read, `w` write (erases!), `a` append | Read only. Safe. Cannot damage their data. |
| `encoding="utf-8"` | **Keyword parameter.** How bytes on disk map to characters | Prevents crashes on names, emoji, non-English characters |
| `with ... as f` | **Context manager.** Auto-closes the file even if the code crashes | `f` = the open file handle. When the indented block ends, the file is closed for you |
| `f` | Variable holding the file object | Fed into the CSV reader below |

**Beginner trap to name:** `"w"` instead of `"r"` silently *empties* their file. Say it once, loudly.

**Why `with`?** Without it you must remember `f.close()`. Humans forget. `with` never forgets.

---

```python
    reader = csv.DictReader(f)
    for row in reader:
        instagram_list.append(int(row["Instagram_Minutes"]))
        study_list.append(int(row["Study_Minutes"]))
```

| Item | In general | In this code |
|---|---|---|
| `csv.DictReader` | Reads each CSV row as a **dictionary**, using the header row as keys | Lets you write `row["Study_Minutes"]` instead of `row[3]` — readable, and survives column reordering |
| `f` (parameter) | The open file object to read from | Our handle |
| `for row in reader:` | **Loop.** Runs the block once per row | One pass per day of data |
| `row` | Loop variable — one dictionary per row | `{"Date": "...", "Instagram_Minutes": "95", ...}` |
| `row["Instagram_Minutes"]` | **Key lookup** in a dictionary | Pulls that one cell. **Comes back as TEXT — `"95"`, not `95`.** |
| `int()` | Built-in that converts to a whole number | Turns the text `"95"` into the number `95` so maths works |
| `.append(value)` | **List method.** Adds one item to the end | Grows the bucket one day at a time |

> **The single most important sentence in this block:**
> *"A CSV file has no idea what a number is. Everything in it is text. `int()` is the translator."*
> Demo it: delete `int()` and show `"95" + "40"` giving `"9540"`.

**Why `.append()` and not `=`?** `=` replaces. `.append()` adds. Students who write `instagram_list = int(...)` end up with one value, not seven.

---

```python
instagram_list = instagram_list[0:7]
study_list = study_list[0:7]
```

| Item | In general | In this code |
|---|---|---|
| `[0:7]` | **Slice.** Start at 0, stop *before* 7 | Keeps exactly 7 days — same 7 days as Step 2, so the comparison is honest |
| Reassignment | The name tag is moved onto the new, shorter list | Old longer list is discarded |

**Foreshadow it:** "Notice `0:7` gives seven items, not eight. Park that. Part D explains it."

---

## 3. PART A — BUILD THE TRAY

```python
instagram = np.array(instagram_list)
study = np.array(study_list)
```

| Item | In general | In this code |
|---|---|---|
| `np.array()` | **Constructor function.** Builds a NumPy array from a list | Converts the shopping bag into a calculator tray |
| parameter | Any sequence — list, tuple, nested list | Our 7-item list of ints |
| Return | A new `ndarray` object | Stored under the clean name `instagram` |

**List vs array — the table to put on the board:**

| | Python list | NumPy array |
|---|---|---|
| Can hold | anything mixed | **one type only** |
| Maths on all items | needs a loop | one instruction |
| Speed | slow | fast (C under the hood) |
| Analogy | shopping bag | calculator tray |

```python
print("Instagram array:", instagram)
```

| Item | In general | In this code |
|---|---|---|
| `print()` | Displays things on screen | Proof the conversion worked |
| Multiple arguments | `print(a, b)` prints both, separated by a space | Label + value |
| `print()` empty | Prints a blank line | Visual breathing room between sections |

**Point at the screen:** no commas between the numbers in an array — `[95 40 120]`, not `[95, 40, 120]`. That missing comma is how you spot an array at a glance.

---

## 4. PART B — THE REPLACEMENT TABLE *(emotional peak — slow down)*

```python
total   = instagram.sum()
average = instagram.mean()
highest = instagram.max()
lowest  = instagram.min()
days    = len(instagram)
```

| Item | In general | In this code | Replaces |
|---|---|---|---|
| `.sum()` | Adds every element | Total Instagram minutes across 7 days | 4 lines of loop |
| `.mean()` | Arithmetic average = sum ÷ count | True average, decimals intact | 2 lines |
| `.max()` | Largest element | Worst scrolling day | 5 lines |
| `.min()` | Smallest element | Best day | 5 lines |
| `len()` | **Function**, not a method. Counts items | Number of days = 7 | — |

**Note the asymmetry and say it:** `.sum()` is a *method* (the array owns it). `len()` is a *function* (works on lists, strings, dicts, arrays — anything with a length). That is why one has a dot and one does not.

**Parameters:** all four take *no* arguments here — the array already knows its own contents. (Later, in 2-D, they take `axis=0` / `axis=1`. Mention, don't teach.)

**Callback to Bug 3:**
> "NumPy does not guess which kind of division you meant. `.mean()` gives the true average, decimals and all."

Contrast on screen: `//` floor division threw the decimals away. `.mean()` does not.

**16 lines → 4 lines.** Write that on the board. Let it sit.

---

## 5. PART C — INDEXING *(budget 5 min)*

```python
instagram[0]     # first
instagram[-1]    # last
instagram[2]     # third
```

| Item | In general | In this code |
|---|---|---|
| `[ ]` after a variable | **Subscript / index operator.** "Give me the item at this position." | Pulls one single number out |
| Index `0` | Counting starts at zero | Day 1 |
| Index `2` | Third position | Day 3 — **this is where they trip** |
| Index `-1` | Counts backwards from the end | Last day, without knowing the length |
| `-2` | Second from the end | (used in Part D) |

**The mental model that fixes zero-indexing forever:**
> "The index is not *which item*. It is *how many steps you walk from the front door*. You are already at item one when you have walked zero steps."

**Run the two questions exactly as scripted:**
1. "Which index is the third day?" → most say 3 → let them be wrong → reveal 2.
2. "How would you get the last day without knowing the length?" → wait → do not hand over `-1`.

**Error to provoke deliberately:** `instagram[7]` → `IndexError: index 7 is out of bounds for axis 0 with size 7`. Read the message aloud word by word. "Size 7, so the last legal index is 6."

---

## 6. PART D — SLICING *(budget 8 min — confuses more than indexing)*

```python
instagram[0:3]    # items 0,1,2   -> 3 values
instagram[-2:]    # last 2 values
instagram[1:4]    # items 1,2,3   -> 3 values
```

**The syntax:** `array[start : stop]`

| Part | In general | Rule |
|---|---|---|
| `start` | First index included | **Inclusive** |
| `stop` | Where to stop | **EXCLUSIVE — not included** |
| missing `start` | Defaults to 0 | `[:3]` = first three |
| missing `stop` | Defaults to the end | `[-2:]` = last two |
| (`step`, 3rd slot) | `[::2]` every 2nd item | Mention only if time allows |

**The arithmetic shortcut that ends the confusion:**
> **Number of values returned = stop − start.**
> `0:3` → 3. `1:4` → 3. `0:7` → 7. Every time.

**Always predict before running.** Ask "how many values come back?" on all three lines *before* pressing run.

**Callback to Bug 4 — say it out loud, do not skip:**
> "Remember `Days: 6` when we expected 7? Same rule. Same trap. Now you know why."

This callback is the entire reason Bug 4 exists earlier in the day.

**Indexing vs slicing — one-line difference:**
`instagram[2]` → a single number. `instagram[2:3]` → an array containing one number. Different things. Show both outputs side by side.

---

## 7. PART E — VECTORISATION *(the big moment)*

```python
hours = instagram / 60
print("Hours per day:", hours.round(2))

difference = study - instagram
print("Study minus Instagram:", difference)
```

| Item | In general | In this code |
|---|---|---|
| `array / 60` | **Broadcasting.** A single number is applied to every element | All 7 minute-values become hours in one go |
| `study - instagram` | **Element-wise operation.** Position 1 with position 1, position 2 with position 2… | 7 daily differences, one per day |
| `.round(2)` | Rounds every element | `2` = **number of decimal places** (the only parameter) |
| `hours` | Variable holding a new array | Original `instagram` is untouched — these operations return a **new** array |

**Say this, word for word:**
> "Two arrays. One minus sign. Seven answers. In Step 2 that was a loop. Here it is one character."

**Non-negotiable warning:** element-wise subtraction requires both arrays to be the **same length**. Different lengths → error. This is why we trimmed both to 7 earlier. Tie the two moments together.

**Ask:** "If a value is negative, what does that mean about that day?" → *scrolled more than studied.* Let **them** say it. Do not say it for them.

---

## 8. PART F — BOOLEAN MASKING *(show True/False FIRST)*

```python
gate = instagram > 100
print("The gate (True/False):", gate)
```

| Item | In general | In this code |
|---|---|---|
| `array > 100` | **Element-wise comparison.** Returns an array of `True`/`False`, same length | 7 answers to "was this day over 100 minutes?" |
| `gate` | Variable holding the boolean mask | Named *gate* on purpose — see the metaphor below |

> **Do not skip to filtering.** Print the mask on its own first. Students must *see* `[True False True ...]` before it becomes useful. This is the single highest-value 60 seconds in Part F.

```python
heavy_days = instagram[instagram > 100]
```

| Item | In general | In this code |
|---|---|---|
| `array[boolean_array]` | **Boolean indexing.** Keeps only positions where the mask is `True` | The heavy-scrolling days |

**The metaphor:** *Filter = Security Gate. True passes. False stays outside.*
Physically walk the line: read the mask left to right, and for each `True` say "in", each `False` say "out".

```python
how_many = (instagram > 100).sum()
```

| Item | In general | In this code |
|---|---|---|
| `.sum()` on booleans | `True` counts as **1**, `False` as **0** | Counting becomes addition |
| The brackets `( )` | Force the comparison to finish *first*, then call `.sum()` on the result | Without them the code reads wrong |

**Why this is beautiful:** counting without a counter variable.

```python
above_average = instagram[instagram > average]
```

| Item | In general | In this code |
|---|---|---|
| Comparing against a variable | The threshold need not be a hard-coded number | Each student filters against **their own** average from Part B — personal data, personal result |

**Callback to Bug 5:**
> "No counter variable. Nothing to reset by mistake. The bug from this morning cannot happen here."

---

## 9. PART G — THE TRAP THAT CREATES PANDAS

```python
mixed = np.array(["2026-09-01", "Instagram", 95])
print("Mixed array:", mixed)
print("Data type:  ", mixed.dtype)
```

| Item | In general | In this code |
|---|---|---|
| `np.array([...])` with mixed types | NumPy must pick **one** type for the whole array | Forced to choose between text and number |
| **Type coercion** | When forced to choose, NumPy promotes everything to the most general type — text | The `95` becomes `'95'` |
| `.dtype` | **Attribute (no brackets!).** Reports the array's single data type | Prints something like `<U10` = Unicode string, max 10 characters |

**Let it fail in front of them. The failure is the lesson.**

**Point at the output:** *"Everything is now text. The 95 has quote marks around it. The number stopped being a number."*

**Prove the damage:** try `mixed.sum()` or `mixed[2] * 2` → `'9595'` or an error. The maths engine is gone.

**Callback to Bug 6:**
> "This is exactly this morning's bug — but now you know WHY. A NumPy array wants ONE kind of thing."

**The closing question — then stop talking:**
> "Your CSV has dates, names AND numbers. So what do you need?"

Wait. Someone will say *a table*. **That** is the door to Step 6. Do not open it yourself.

---

## 10. FULL INVENTORY — quick lookup while teaching

### Variables
| Name | Holds | Created in |
|---|---|---|
| `instagram_list`, `study_list` | Python lists of ints | Loading |
| `f` | Open file object | Loading |
| `reader` | `DictReader` object | Loading |
| `row` | One row as a dictionary | Loop |
| `instagram`, `study` | NumPy arrays, 7 values each | Part A |
| `total`, `average`, `highest`, `lowest` | Single numbers | Part B |
| `days` | Integer, 7 | Part B |
| `hours` | New array, minutes ÷ 60 | Part E |
| `difference` | New array, study − instagram | Part E |
| `gate` | Boolean array | Part F |
| `heavy_days`, `above_average` | Filtered arrays | Part F |
| `how_many` | Integer count | Part F |
| `mixed` | Array of strings (the trap) | Part G |

### Functions (standalone — no dot)
`open()` · `int()` · `len()` · `print()` · `np.array()` · `csv.DictReader()`

### Methods (belong to an object — dot before them)
`.append()` · `.sum()` · `.mean()` · `.max()` · `.min()` · `.round(n)`

### Attribute (no brackets)
`.dtype`

### Operators doing heavy lifting
`/` broadcast division · `-` element-wise subtraction · `>` element-wise comparison · `[ ]` index, slice **and** boolean filter

---

## 11. THE COMPARISON TABLE *(fill on the board with them)*

| | Plain Python | NumPy |
|---|---|---|
| total / average / max / min | 16 | 4 |
| days above average | 5 | 1 |
| convert all to hours | 4 | 1 |
| places a silent bug can hide | many | few |

**Close with the spine sentence:** *NumPy = Fast Math Engine. One instruction. Many numbers.*

---

## 12. ERRORS TO PROVOKE ON PURPOSE (if you have spare minutes)

| Break this | Error / result | Lesson |
|---|---|---|
| Remove `int()` | `'9540'` instead of `135` | CSV gives text |
| `instagram[7]` | `IndexError ... size 7` | Last index is 6 |
| `instagram[0:3]` expecting 4 | 3 values | Stop is exclusive |
| Subtract arrays of different length | `ValueError: operands could not be broadcast` | Lengths must match |
| `mixed.dtype()` | `TypeError: not callable` | Attribute ≠ method |
| `mixed.sum()` | joins text / errors | One type per array |
