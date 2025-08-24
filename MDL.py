import streamlit as st
from time import sleep

st.set_page_config(
    page_title="MDL editor", page_icon="🧑‍💻"
)

st.title("DML code editor")

stop = st.toggle("Stop running code at errors?")

user_input = st.text_area("Enter code:")

output_placeholder = st.empty()


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
                elif line[0:6] == "<line>":
                    st.markdown("---")
                elif line[0:3] == "<G>":
                    st.success(line[3:])
                elif line[0:3] == "<R>":
                    st.error(line[3:])
                elif line[0:3] == "<B>":
                    st.info(line[3:])
                elif line[0:8] == "<python>":
                    st.markdown(f"""```python
                    {line[8:]}""")
                elif line[0:7] == '<write>':
                    line = line.replace("£££", "***")
                    line = line.replace("££", "**")
                    line = line.replace("£", "_")
                    line = line.replace("~", "`")
                    line = line.replace("..", "~~")
                    line = line.replace("*/*", "```")
                    line = line.replace(">>>", "•")
                    line = line.replace("Ra|", ":rainbow[")
                    line = line.replace("Gr|", ":green[")
                    line = line.replace("Bl|", ":blue[")
                    line = line.replace("Re|", ":red[")
                    line = line.replace("||", "]")
                    line = line.replace("!*!", "```")
                    st.markdown(f"{i+1}: {line[7:]}")
                else:
                    if stop:
                        st.error(f"Line {i+1}: error. Code stopped")
                        st.stop()
                    else:
                        st.error(f"Line {i+1}: error")      
            st.markdown("---")            
            st.info("Code finished")            
    else:
        output_placeholder.empty()
        st.warning("Please enter code.")
