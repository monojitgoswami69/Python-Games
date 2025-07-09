# 🎮 Python-Games
A fun little terminal-based Python project by **MG** 

---

## 🚀 What's Inside?

### 🕹️ Rock Paper Scissors (RPS)
A fully interactive terminal game located in `RPS/RockPaperScissors.py`.

**Features:**
- ⌨️ User input with validation
- 🎨 Color-coded output using ANSI escape codes
- ⏱ Countdown animations with typewriter-style text printing
- 📊 Live scoreboard with round tracking
- 🤖 Computer AI with emoji-powered choices
- 🧠 End-game stats with total wins, losses, and ties
- 🔇 Input suppression during terminal animations to prevent accidental typing

---

### 🌀 RPS: Reversed Logic Edition
Located in `RPS/RockPaperScissors_Reversed.py`  
This is the **OG Rock Paper Scissors... but unhinged**.

All features from the original RPS game apply — same interface, same animations, same sarcasm **except**:
- 🌀 **Reversed logic** (Scissors beats Rock?! WHAT?!)
- 🎭 **Chaos Mode enabled:** 
>✂️ Scissors absolutely destroy Rock because why not   
>🪨 Rock drills a hole into Paper's soul  
>📄 Paper wraps Scissors like a burrito of defeat
- 🧪 Pure chaos, zero reason — maximum entertainment

---

### 🔐 Input Suppressor Utility
Located in `Input_suppressor/input_suppressor.py`  
A cross-platform input suppressor using `msvcrt` (Windows) and `termios/tty` (Unix/macOS/Linux).

**Purpose:**
> Prevents the user from accidentally typing during animated sequences (like countdowns or cinematic intros).

**How to use:**
```python
from Input_suppressor.input_suppressor import suppress_input

with suppress_input():
    # Block keyboard input during this block
