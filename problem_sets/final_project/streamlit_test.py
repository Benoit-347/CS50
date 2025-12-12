# this is a program to test how streamlit handles buttons, how it executes the whole code from start to end: at first once, then every time the submit button is pressed-
# the every same session the button's true state is copied and whole code is executed.
    # Here it hence maintains an infinite loop (until we specify a code to end the program explicitly)

import streamlit

# by running this program, you may notice, at each session, the code before button is executed regarless of button input, the end is also executed regardless of button input.
# only the state of the pressed button changes in each session. We can take advantage of this state change (which occurs in each session post start of program) by applying a if statement on the button.
    # this causes the code under if block to only execute if the button was pressed, in each session.
# the session runs in this order: First the whole code runs, with default button states. THen on each button press, the whole code is run again; maintaining the button that triggered the rerun. And the session_state obj maintains data accross every session (more universally accessible than the prgram's global)
if "counter_end" not in streamlit.session_state:
    streamlit.session_state.counter_end = 0
if "counter_start" not in streamlit.session_state:
    streamlit.session_state.counter_start = 0

streamlit.session_state.counter_start += 1
print("Now, reached Starting part of code!\n" + str(streamlit.session_state.counter_start) + " times")
streamlit.write("Now, reached Starting part of code!\n" + str(streamlit.session_state.counter_start) + " times")

with streamlit.form(key = f"This is an argument passed to var key of form"):
    button_1 = streamlit.form_submit_button("Button submit_1")
    button_2 = streamlit.form_submit_button("Button submit_2")

    if button_1:
        print("First button pressed")
        streamlit.write("First button pressed")

    if button_2:
        print("Secong button pressed")
        streamlit.write("Second button pressed")

streamlit.session_state.counter_end += 1
print("Remanining code executed!\n" + str(streamlit.session_state.counter_end) + " times")
streamlit.write("Remanining code executed!\n" + str(streamlit.session_state.counter_end) + " times")