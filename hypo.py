import streamlit as st
from time import sleep

st.title("Dosh code editor")

user_input = st.text_area("Enter code:")

output_placeholder = st.empty()

stop = st.toggle("Stop running code at errors?")

if st.button("Run:"):
    if user_input:
        with output_placeholder.container():
            st.subheader("Output:")
            lines = user_input.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                if line[0:5] == "<ask>":
                    answer = st.text_area(f"{i+1}: {line[5:]}")
                elif line[0:7] == "<alert>":
                    st.toast(line[7:])
                elif line[0:10] == "<balloons>":
                    st.balloons()
                elif line[0:6] == "<snow>":
                    st.snow()
                elif line[0:7] == "<check>":
                    if answer == line[7:]:
                        st.success("")
                    else:
                        st.error("")
                elif line[0:6] == "<wait>":
                    sleep(int(line[6:]))
                elif line[0:9] == "<spinner>":
                    with st.spinner():
                        sleep(int(line[9:]))
                elif line[0:7] == '<write>':
                    st.write(f"{i+1}: {line[7:]}")
                else:
                    if stop:
                        st.error(f"Line {i+1}: error. Code stopped")
                        st.stop()
                    else:
                        st.error(f"Line {i+1}: error")
    else:
        output_placeholder.empty()
        st.warning("Please enter code.")
