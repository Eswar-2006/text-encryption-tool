# 🔑 Caesar Cipher – Text Encryption & Decryption

The **Caesar Cipher** is one of the oldest and simplest encryption techniques, invented by Julius Caesar.  
It is a **substitution cipher** where each letter in the message is shifted by a certain number of positions in the alphabet.  

This Python project implements a **Caesar Cipher tool** that allows users to:
- 🔒 **Encrypt** a message with a custom shift value.
- 🔓 **Decrypt** a message back to its original form using the same shift value.

---

## 📖 How It Works
- Each character in the input message is shifted forward (for encryption) or backward (for decryption) by a given number of positions.  
- The alphabet is considered **circular** (after `Z` comes `A`).  
- Non-alphabet characters (spaces, numbers, punctuation) can either be kept as they are or extended for encryption depending on the implementation.  

**Example (Shift = 3):**
- Plain text: `HELLO`
- Encrypted text: `KHOOR`

---

## 🚀 Features
- Encrypts plain text messages with a custom shift value.
- Decrypts encrypted text back to the original form.
- Handles both **uppercase and lowercase** letters.
- Ignores non-alphabet characters (e.g., numbers, punctuation remain unchanged).
- CLI-based program – lightweight and easy to use.
- No external libraries required (only built-in Python).

---

## 📂 Project Structure
