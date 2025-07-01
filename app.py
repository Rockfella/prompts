
import streamlit as st
import random

st.set_page_config(page_title="Daily Health Prompts", layout="centered")

st.title("🧠 Daily Health Prompts")
st.markdown("Take a screenshot to save your daily card. Tap a button to re-randomize a question.")

# Define the categories and prompts
categories = {
    "Fitness & Movement": [
        "What’s a 10-minute stretching routine I can do at my desk to relieve back tension?",
        "What’s one low-impact cardio workout I can do at home without equipment?",
        "What’s a strength training routine I can do in 20 minutes using only body weight?",
        "What’s a quick workout I can do during a lunch break to boost my energy?",
        "What’s a beginner-friendly yoga flow I can do to wind down before bed?",
        "What’s a walking route I can take near my home that includes some hills?",
        "What’s a 15-minute workout I can do in my living room with no jumping?",
        "What’s a simple mobility routine I can do every morning to loosen up?",
        "What’s a fun dance workout I can try today to get my heart rate up?"
    ],
    "Health Tracking & Goals": [
        "What’s a realistic step goal I can set for today?",
        "What’s a way to track my water intake without an app?",
        "What’s a weekly health goal I can set that feels achievable?",
        "What’s a way to measure progress without using a scale?",
        "What’s a habit tracker I can use to stay consistent with my workouts?",
        "What’s a way to celebrate small health wins this week?",
        "What’s a monthly check-in I can do to reflect on my wellness goals?",
        "What’s a way to track my mood and energy levels over time?",
        "What’s a simple system for logging my meals without calorie counting?",
        "What’s a way to visualize my health progress that keeps me motivated?"
    ],
    "Nutrition & Eating Habits": [
        "What’s a healthy breakfast I can make in under 10 minutes?",
        "What’s one high-protein snack I can prep for the week?",
        "What’s a simple way to add more fiber to my lunch today?",
        "What’s a plant-based dinner I can cook in 30 minutes or less?",
        "What’s a hydration goal I can set for today based on my activity level?",
        "What’s a creative way to use leafy greens in my meals this week?",
        "What’s a balanced meal I can pack for work that doesn’t need reheating?",
        "What’s a healthy grocery list for someone cooking for two?"
    ],
    "Lifestyle & Daily Habits": [
        "What’s a healthy morning routine I can try?",
        "What’s a way to make my commute more active?",
        "What’s a healthy habit I can stack onto my coffee routine?",
        "What’s a way to stay active on a rainy day?",
        "What’s a healthy habit I can do in under 2 minutes?",
        "What’s a way to make my weekend more restorative?",
        "What’s a way to reduce screen time without feeling disconnected?",
        "What’s a way to build more movement into my workday?"
    ],
    "Mental Health & Mindfulness": [
        "What’s a 5-minute breathing exercise I can do to reduce anxiety?",
        "What’s the best (5min) way to extract flow and being in the now?",
        "What’s a mindfulness practice I can try during my commute?",
        "What’s a calming ritual I can add to my bedtime routine?",
        "What’s a way to check in with my emotions during a busy day?",
        "What’s a screen-free activity I can do tonight to relax my mind?",
        "What’s a grounding technique I can use when I feel overwhelmed?",
        "What’s a simple gratitude practice I can start today?",
        "What’s a way to create a calming space in my home for mental breaks?",
        "What’s a short meditation I can do before a stressful meeting?"
    ],
    "Social & Emotional Wellness": [
        "What’s a way to connect with a friend that supports both our health?",
        "What’s a way to set boundaries that protect my mental health?",
        "What’s a way to ask for support when I’m feeling low?",
        "What’s a way to make shared meals healthier without being restrictive?",
        "What’s a way to talk to my partner about our health goals?",
        "What’s a way to support a loved one going through a health challenge?",
        "What’s a way to make group workouts more fun and inclusive?",
        "What’s a way to express appreciation to someone who supports my wellness?",
        "What’s a way to build a support system for my health journey?",
        "What’s a way to stay socially connected while prioritizing rest?"
    ],
    "Sleep & Recovery": [
        "What’s a wind-down routine I can try to fall asleep faster tonight?",
        "What’s one habit I can change to improve my sleep quality this week?",
        "What’s a caffeine cut-off time that could help me sleep better?",
        "What’s a relaxing playlist I can listen to before bed?",
        "What’s a gentle stretch I can do in bed to help me fall asleep?",
        "What’s a sleep tracker I can use to understand my patterns better?",
        "What’s a breathing technique I can use if I wake up in the middle of the night?"
    ],
    "Motivation & Mindset": [
        "What’s a mantra I can use today to stay focused on my health goals?",
        "What’s a way to reframe a health setback as a learning moment?",
        "What’s a way to stay motivated when I don’t see immediate results?",
        "What’s a way to make health changes feel less overwhelming?",
        "What’s a way to build confidence in my ability to make healthy choices?",
        "What’s a way to stay consistent when life gets busy?",
        "What’s a way to remind myself why I started my health journey?",
        "What’s a way to make my health goals more enjoyable?",
        "What’s a way to track non-scale victories in my wellness journey?",
        "What’s a way to reset my mindset after a tough day?"
    ],
    "Preventive Health & Wellness": [
        "What’s one health screening I should schedule this year based on my age?",
        "What’s a way to motivate me taking the blood pressure more often?",
        "What’s a daily habit i can do today that supports heart health?",
        "What’s a way to protect my skin from sun damage during outdoor workouts?",
        "What’s a simple way to improve my posture while working?",
        "What’s a way to reduce my sitting time during the workday?",
        "What’s a tip for keeping my immune system strong during flu season?",
        "What’s a way to monitor my hydration levels throughout the day?",
        "What’s a reminder system I can use to take my medications on time?"
    ]
}

# Initialize session state for each category
for cat in categories:
    if cat not in st.session_state:
        st.session_state[cat] = random.choice(categories[cat])

# Display each category and its question with a re-randomize button
for cat in categories:
    st.subheader(cat)
    st.markdown(f"**{st.session_state[cat]}**")
    if st.button(f"🔄 New question for {cat}"):
        st.session_state[cat] = random.choice(categories[cat])
        st.experimental_rerun()
