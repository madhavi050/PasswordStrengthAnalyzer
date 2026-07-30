# Password Strength Analyzer

A Python-based cybersecurity tool that analyzes password strength and generates strong passwords using password security principles.

## Features

- Analyze password strength
- Generate strong random passwords
- Display password score
- Estimate password crack time
- Provide password improvement suggestions
- User-friendly graphical interface using Tkinter

## Technologies Used

- Python
- Tkinter
- zxcvbn Library

## Project Structure

```
PasswordStrengthAnalyzer
│
├── analyzer.py
├── generator.py
├── gui.py
├── main.py
├── requirements.txt
├── .gitignore
└── output/
```

## Installation

1. Clone the repository

```
git clone <repository-url>
```

2. Install required libraries

```
pip install -r requirements.txt
```

## Usage

Run the GUI application:

```
python gui.py
```

or run the command-line version:

```
python main.py
```

## How It Works

1. User enters a password or generates a password.
2. The analyzer evaluates password strength.
3. The tool provides:
   - Strength score
   - Crack time estimation
   - Security suggestions

## Author

Madhavi Sabade
