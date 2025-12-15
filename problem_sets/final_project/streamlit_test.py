# this is a program to test how streamlit handles buttons, how it executes the whole code from start to end: at first once, then every time the submit button is pressed-
# the every same session the button's true state is copied and whole code is executed.
    # Here it hence maintains an infinite loop (until we specify a code to end the program explicitly)

import streamlit
import time # for sleep fn

# by running this program, you may notice, at each session, the code before button is executed regarless of button input, the end is also executed regardless of button input.
# only the state of the pressed button changes in each session. We can take advantage of this state change (which occurs in each session post start of program) by applying a if statement on the button.
    # this causes the code under if block to only execute if the button was pressed, in each session.
# the session runs in this order: First the whole code runs, with default button states. THen on each button press, the whole code is run again; maintaining the button that triggered the rerun. And the session_state obj maintains data accross every session (more universally accessible than the prgram's global)

    # session_state main
if "counter_end" not in streamlit.session_state:
    streamlit.session_state.counter_end = 0
if "counter_start" not in streamlit.session_state:
    streamlit.session_state.counter_start = 0

streamlit.session_state.counter_start += 1
print("Now, reached 'Starting part of code!'" + str(streamlit.session_state.counter_start) + " times")
streamlit.write("Now, reached Starting part of code!\n" + str(streamlit.session_state.counter_start) + " times")

with streamlit.form(key = f"This is an argument passed to var key of form"):
    # a text can be input only inside a form; and every input mandatorily needs a button (as when the form closes, the input is lost; hence if no button was triggered brefore form closes, the input becomes useless; hence streamlit making it mandatory).

    streamlit.write("inside form")
    streamlit.title("columns test")
    # this creates 2 boxes top one and bottom one, returns its ids, which you can use to send it feature info
    col_1, col_2 = streamlit.columns(2)
    
    col_1 = streamlit.text_input("Enter text 1: ")
    col_2 = streamlit.text_input("Enter text 2: ")

    streamlit.write(col_1)

    streamlit.title("Spinner test")
    with streamlit.spinner("Spining animation..."):     # use this to show a replaceable text. (replaced by the text in .success() method)
        time.sleep(3)
    streamlit.success("Spinning completed")

    streamlit.title("buttons test")
    # protrays two buttons, which has functionality: if pressed, triggers a rerun of this program, sending this button's state to next session. (may be used along with if statement, using its real functionality)
    button_1 = streamlit.form_submit_button("Button submit_1")
    button_2 = streamlit.form_submit_button("Button submit_2")

    if button_1:
        print("First button pressed")
        streamlit.write("First button pressed")

    if button_2:
        print("Secong button pressed")
        streamlit.write("Second button pressed")
    
    streamlit.write("last line of form")

# notice these filters are outside the forms space. We cannot apply checkbox + sliders inside a form
streamlit.title("filters test")

if streamlit.checkbox("filter_1"):
    filter_1_value = streamlit.slider("filter_1 value: ", 0, 100, 1)

if streamlit.checkbox("filter_2"):
    filter_2_value = streamlit.slider("filter_2 value: ", 0, 100, 1)


# setting up fig from matplot lib, to display onto streamlit-
import matplotlib.pyplot as plt
import numpy as np

# 1. Data (Simple Sine Wave)
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. Setup Plot
fig, ax = plt.subplots(figsize=(10, 4))

# 3. Plotting (Line + Soft Fill)
ax.plot(x, y, color='#2e86de', linewidth=2)
ax.fill_between(x, y, color='#2e86de', alpha=0.1)

# 4. "Elegant" Styling (Removing the boxy borders)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_title("Waveform Analysis", fontsize=14, loc='left')
ax.grid(axis='y', linestyle='--', alpha=0.3) # Subtle grid

# 5. Render in Streamlit
streamlit.pyplot(fig, use_container_width=True)


streamlit.session_state.counter_end += 1
print("'Remaining code executed!'" + str(streamlit.session_state.counter_end) + " times")
streamlit.write("Remanining code executed!\n" + str(streamlit.session_state.counter_end) + " times")