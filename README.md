

---

# Chatbot Project

## Introduction

This project is a chatbot application designed to provide responses based on predefined patterns and JSON-based response data. It includes both a command-line interface and a graphical user interface (GUI) for user interaction.

---

## Step-by-Step Development Process

### 1. **Setting Up the Environment**
   - **Installed Python**: Ensured Python (version 3.x) was installed.
   - **Created Virtual Environment**:
     ```bash
     python -m venv .venv
     ```
     Activated the virtual environment to manage dependencies.

   - **Installed Required Libraries**:
     Dependencies were listed in `requirements.txt`. Installed them using:
     ```bash
     pip install -r requirements.txt
     ```

---

### 2. **Defining Project Scope**
   - Decided to build a chatbot that:
     - Processes user inputs.
     - Matches patterns using custom scripts.
     - Offers a GUI for ease of use.

---

### 3. **Data Preparation**
   - **`responses.json`**: Created a JSON file to store predefined responses for various input patterns.
   - **`dialogs.txt`**: Used this text file for testing and debugging conversational flows.

---

### 4. **Implementing Core Logic**
   - **Pattern Matching (`pattern_matching.py`)**:
     - Wrote a script to identify user input patterns and fetch appropriate responses from `responses.json`.
   - **Main Chatbot Logic (`chatbot.py`)**:
     - Combined the pattern-matching script with input handling.
     - Tested the logic using command-line interactions.

---

### 5. **Building the GUI**
   - Created a graphical interface using **Tkinter** in `gui_chatbot.py`.
   - Implemented:
     - Input field for user messages.
     - Scrollable chat history.
     - Dynamic response display.

---

### 6. **Testing and Debugging**
   - Verified:
     - Input-output consistency.
     - Pattern matching accuracy.
     - GUI usability.

   - Fixed issues like:
     - Incorrect response retrieval.
     - GUI crashes due to unhandled exceptions.

---

### 7. **Version Control**
   - **Git**: Initialized a Git repository to track changes.
   - **.gitattributes and .gitignore**: Configured Git to exclude the virtual environment and cache files.

---

### 8. **Documentation**
   - **README.md**: Created to explain the project structure and usage.
   - Added comments in scripts to make the code self-explanatory.

---

## Requirements
- Python 3.x
- Libraries in `requirements.txt`:
  ```text
  tkinter
  json
  re
  other_dependencies...
  ```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Chatbot
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Linux/Mac
   .\.venv\Scripts\activate   # On Windows
   ```
4. Run the chatbot:
   - For command-line interface:
     ```bash
     python chatbot.py
     ```
   - For GUI:
     ```bash
     python gui_chatbot.py
     ```

---

## Challenges Faced
- Handling ambiguous user inputs.
- Debugging pattern-matching logic.
- Designing an intuitive GUI layout.

---
 
