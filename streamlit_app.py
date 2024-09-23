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
if 'game_over' not in st.session_state:
    st.session_state['game_over'] = False

if st.session_state['upper_limit'] is None:
    upper_limit = st.number_input("Enter an upper limit", min_value=10, max_value=1000000, step=1, value=100)
    if st.button("Set Upper Limit"):
        st.session_state['upper_limit'] = upper_limit
        st.session_state['max_val'] = upper_limit
        st.session_state['tries_left'] = math.ceil(math.log2(upper_limit))
        st.success(f"I will guess your number within {st.session_state['tries_left']} tries!")
else:
    st.write(f"Upper Limit set to: {st.session_state['upper_limit']}")
    st.write(f"I will find your number within {st.session_state['tries_left']} tries!")

    if st.session_state['mid_val'] is None:
        st.session_state['mid_val'] = (st.session_state['min_val'] + st.session_state['max_val']) // 2

    if not st.session_state['game_over']:
        st.write(f"My guess is: {st.session_state['mid_val']}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Your number is smaller (MIN)"):
                st.session_state['max_val'] = st.session_state['mid_val'] - 1
                st.session_state['tries_left'] -= 1

        with col2:
            if st.button("Your number is larger (MAX)"):
                st.session_state['min_val'] = st.session_state['mid_val'] + 1
                st.session_state['tries_left'] -= 1

        # Calculate new mid_val
        if st.session_state['tries_left'] > 0:
            st.session_state['mid_val'] = (st.session_state['min_val'] + st.session_state['max_val']) // 2
        
        # Check if the number is found
        if st.session_state['min_val'] == st.session_state['max_val']:
            st.success(f"I found your number! It is {st.session_state['min_val']}. I won!")
            st.session_state['game_over'] = True
        elif st.session_state['tries_left'] == 0:
            st.error("I've run out of tries! You won!")
            st.session_state['game_over'] = True
    else:
        st.write("Game Over!")
        if st.button("Restart Game"):
            for key in st.session_state.keys():
                del st.session_state[key]
