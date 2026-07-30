import tkinter as tk
from tkinter import messagebox

from analyzer import analyze_password
from generator import generate_password


def analyze():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a password"
        )
        return


    result = analyze_password(password)


    score_label.config(
        text=f"Score: {result['score']}"
    )

    strength_label.config(
        text=f"Strength: {result['strength']}"
    )

    crack_label.config(
        text=f"Crack Time: {result['crack_time']}"
    )


    suggestions_box.delete(
        "1.0",
        tk.END
    )


    for suggestion in result["suggestions"]:
        suggestions_box.insert(
            tk.END,
            "• " + suggestion + "\n"
        )



def generate():

    password = generate_password(12)

    password_entry.delete(
        0,
        tk.END
    )

    password_entry.insert(
        0,
        password
    )


# Window
window = tk.Tk()

window.title(
    "Password Strength Analyzer"
)

window.geometry(
    "500x500"
)


# Heading
title = tk.Label(
    window,
    text="Password Strength Analyzer",
    font=("Arial",16,"bold")
)

title.pack(
    pady=20
)


# Password input

password_entry = tk.Entry(
    window,
    width=35,
    font=("Arial",12)
)

password_entry.pack(
    pady=10
)



# Buttons

analyze_button = tk.Button(
    window,
    text="Analyze Password",
    command=analyze,
    width=20
)

analyze_button.pack(
    pady=5
)



generate_button = tk.Button(
    window,
    text="Generate Strong Password",
    command=generate,
    width=20
)

generate_button.pack(
    pady=5
)



# Result labels

score_label = tk.Label(
    window,
    text="Score:"
)

score_label.pack()



strength_label = tk.Label(
    window,
    text="Strength:"
)

strength_label.pack()



crack_label = tk.Label(
    window,
    text="Crack Time:"
)

crack_label.pack()



# Suggestions

suggestions_box = tk.Text(
    window,
    height=8,
    width=50
)

suggestions_box.pack(
    pady=10
)



window.mainloop()