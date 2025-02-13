import tkinter as tk
from tkinter import scrolledtext
import openai

# Configure your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def analyze_cv():
    cv_text = input_text.get("1.0", tk.END)
    if not cv_text.strip():
        result_label.config(text="Please enter a CV to analyze.")
        return
    
    prompt = f"Analyze the following CV and extract the top 10 skills of the candidate:\n{cv_text}\n\nReturn only the skills as bullet points."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an expert assistant in CV analysis."},
                      {"role": "user", "content": prompt}]
        )
        skills = response["choices"][0]["message"]["content"]
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, skills)
    except Exception as e:
        result_label.config(text=f"Error processing: {e}")

# Create main window
window = tk.Tk()
window.title("CV Analyzer")
window.geometry("600x500")

# Instructions label
instructions = tk.Label(window, text="Paste the CV into the text box and press 'Analyze'")
instructions.pack()

# Text box for CV input
input_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=10)
input_text.pack()

# Analyze button
analyze_button = tk.Button(window, text="Analyze", command=analyze_cv)
analyze_button.pack()

# Result label
result_label = tk.Label(window, text="Detected skills:")
result_label.pack()

# Text box for displaying results
result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=10)
result_text.pack()

# Run application
window.mainloop()
