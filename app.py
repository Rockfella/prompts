import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(page_title="Daily Health Prompts", layout="centered")

st.title("🧠 Daily Health Prompts")
st.markdown("Take a screenshot to save your daily card. Tap a button to re-randomize a question.")

# Read the Excel file
df = pd.read_excel("health_prompts.xlsx", engine="openpyxl", header=None)

# Extract categories and prompts from the structured columns
categories = {}

# Iterate through the rows starting from row 3 (index 2)
for index, row in df.iterrows():
    if index < 2:
        continue
    for col in [0, 3]:  # Column 0 and 3 contain categories
        category = row[col]
        prompt = row[col + 1] if col + 1 < len(row) else None
        if pd.notna(category) and pd.notna(prompt):
            if category not in categories:
                categories[category] = []
            categories[category].append(prompt)

# Initialize session state for each category
for cat in categories:
    key = f"prompt_{cat}"
    if key not in st.session_state:
        st.session_state[key] = random.choice(categories[cat])

# Display each category and its question with a re-randomize button
for cat in categories:
    col1, col2 = st.columns([4, 1])
    with col1:
        st.subheader(cat)
        st.markdown(f"**{st.session_state[f'prompt_{cat}']}**")
    with col2:
        if st.button("🔄", key=f"btn_{cat}"):
            st.session_state[f"prompt_{cat}"] = random.choice(categories[cat])
