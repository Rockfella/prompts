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
        padding: 2rem;
        border-radius: 10px;
    }}
    a.prompt-link {{
        font-size: 1.1rem;
        font-weight: bold;
        color: black;
        text-decoration: none;
    }}
    a.prompt-link:hover {{
        text-decoration: underline;
        color: #333;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and date
st.title("🧠 Daily Prompts")
st.markdown(f"### {date_str}")
st.markdown("Click a question to re-randomize it. Take a screenshot to save your daily card.")

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

# Get query params to detect clicks
query_params = st.experimental_get_query_params()
clicked_cat = query_params.get("clicked", [None])[0]

# Initialize session state
for cat in categories:
    key = f"prompt_{cat}"
    if key not in st.session_state:
        st.session_state[key] = random.choice(categories[cat])

# If a category was clicked, update its prompt
if clicked_cat in categories:
    st.session_state[f"prompt_{clicked_cat}"] = random.choice(categories[clicked_cat])
    # Clear the query param to avoid repeated updates
    st.experimental_set_query_params()

# Display each category and its prompt as a clickable link
for cat in categories:
    prompt = st.session_state[f"prompt_{cat}"]
    st.subheader(cat)
    st.markdown(
        f'<a href="?clicked={cat}" class="prompt-link">{prompt}</a>',
        unsafe_allow_html=True
    )
