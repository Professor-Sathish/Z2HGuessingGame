import streamlit as st
import math

st.title("Zero2Hero Python Prediction Game")

# Step 1: Get upper limit from the user
if 'upper_limit' not in st.session_state:
    st.session_state['upper_limit'] = None
if 'min_val' not in st.session_state:
    st.session_state['min_val'] = 1
if 'max_val' not in st.session_state:
    st.session_state['max_val'] = None
if 'mid_val' not in st.session_state:
    st.session_state['mid_val'] = None
if 'tries_left' not in st.session_state:
    st.session_state['tries_left'] = None

if st.session_state['upper_limit'] is None:
    upper_limit = st.number_input("Enter an upper limit", min_value=10, max_value=1000000, step=1, value=100)
    if st.button("Set Upper Limit"):
        st.session_state['upper_limit'] = upper_limit
        st.session_state['max_val'] = upper_limit
        st.session_state['tries_left'] = math.ceil(math.log2(upper_limit))

else:
    st.write(f"Upper Limit set to: {st.session_state['upper_limit']}")
    st.write(f"You have {st.session_state['tries_left']} tries to guess the number.")
    if st.session_state['mid_val'] is None:
        st.session_state['mid_val'] = (st.session_state['min_val'] + st.session_state['max_val']) // 2
    
    st.write(f"My guess is: {st.session_state['mid_val']}")
    
    if st.button("Your number is smaller (MIN)"):
        st.session_state['max_val'] = st.session_state['mid_val'] - 1
        st.session_state['tries_left'] -= 1
    elif st.button("Your number is larger (MAX)"):
        st.session_state['min_val'] = st.session_state['mid_val'] + 1
        st.session_state['tries_left'] -= 1
    
    # Calculate new mid_val
    if st.session_state['tries_left'] > 0:
        st.session_state['mid_val'] = (st.session_state['min_val'] + st.session_state['max_val']) // 2
    
    # Check if the number is found
    if st.session_state['min_val'] == st.session_state['max_val']:
        st.write(f"I found your number! It is {st.session_state['min_val']}")
        st.write("Game Over!")
        if st.button("Restart Game"):
            for key in st.session_state.keys():
                del st.session_state[key]
    elif st.session_state['tries_left'] == 0:
        st.write("You've run out of tries! I couldn't guess your number.")
        if st.button("Restart Game"):
            for key in st.session_state.keys():
                del st.session_state[key]
