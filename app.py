import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Daily Health Prompts", layout="centered")

st.title("🧠 Daily Health Prompts")
st.markdown("Take a screenshot to save your daily card. Tap a button to re-randomize a question.")

# Load Excel file
df = pd.read_excel("health_prompts.xlsx", engine="openpyxl", header=None)

# Extract categories and prompts
categories = {}
for index, row in df.iterrows():
    if index < 2:
        continue
    for col in [0, 3]:
        category = row[col]
        prompt = row[col + 1] if col + 1 < len(row) else None
        if pd.notna(category) and pd.notna(prompt):
            categories.setdefault(category, []).append(prompt)

# Initialize session state
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
            st.query_params["updated"] = cat  # harmless trigger to refresh state
