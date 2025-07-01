import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Daily Prompts", layout="centered")

# Generate two colors based on today's date
today = datetime.today()
date_str = today.strftime("%B %d, %Y")
color1 = f"#{(today.day * 5 % 256):02x}{(today.month * 20 % 256):02x}{(today.year % 256):02x}"
color2 = f"#{(today.month * 15 % 256):02x}{(today.day * 10 % 256):02x}{(today.year * 2 % 256):02x}"

# Inject CSS for gradient background
st.markdown(
    f"""
    <style>
    section.main > div {{
        background: linear-gradient(135deg, {color1}, {color2});
        background-attachment: fixed;
        padding: 1rem;
    }}
    .question-row {{
        margin-bottom: 0.2rem;
    }}
    h3 {{
        margin-bottom: 0.1rem !important;
        margin-top: 0.1rem !important;
        font-size: 1rem;
    }}
    button[kind="secondary"] {{
        all: unset;
        font-size: 0.9rem;
        font-weight: 500;
        color: black;
        cursor: pointer;
    }}
    button[kind="secondary"]:hover {{
        text-decoration: underline;
    }}
    </style>
    """,
    unsafe_allow_html=True
)





# Title and date
st.title(f"🧠 {date_str}")



# Load the Excel file, skip the first row, and read only the first two columns
df = pd.read_excel("prompts.xlsx", engine="openpyxl", header=None, skiprows=1, usecols=[0, 1])
df.columns = ["Category", "Prompt"]

# Group prompts by category
categories = {}
for _, row in df.iterrows():
    category = row["Category"]
    prompt = row["Prompt"]
    if pd.notna(category) and pd.notna(prompt):
        categories.setdefault(category, []).append(prompt)

# Initialize session state
for cat in categories:
    key = f"prompt_{cat}"
    if key not in st.session_state:
        st.session_state[key] = random.choice(categories[cat])

# Define update function
def update_prompt(cat):
    st.session_state[f"prompt_{cat}"] = random.choice(categories[cat])

# Display each category and its question with a re-randomize button
for cat in categories:
    key = f"prompt_{cat}"
    prompt = st.session_state[key]

    st.markdown('<div class="question-row">', unsafe_allow_html=True)

    col1, _ = st.columns([1, 0.01])  # Single column layout
    with col1:
        st.subheader(cat)
        st.button(f"{prompt}", key=f"btn_{cat}", on_click=update_prompt, args=(cat,))

    st.markdown('</div>', unsafe_allow_html=True)







