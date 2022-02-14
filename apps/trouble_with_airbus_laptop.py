import streamlit as st


def app():
    st.subheader("Installation for an Airbus Laptop")
    st.write("Due to Airbus Proxy, it's not possible to download the model with the command:")
    st.code("pipeline('fill-mask', model='distilbert-base-uncased'), language='python'")
    st.write("Hence, you need to download it manually.")
    st.write("You can do it directly here: https://huggingface.co/distilbert-base-uncased/tree/main")
    st.markdown("I had some issue during the download and need to download and copy past some file manually. To ease the process I've put it in the [shared Airbus directory](https://drive.google.com/drive/folders/1WDlZH1cbxMZCW7B5cYjks_mS1sDQMMzC?usp=sharing)")
    st.write("Another possibility is to clone the repository of the model with the shell command:")
    st.code("git clone https://huggingface.co/distilbert-base-uncased", language="shell")
    st.subheader("Remove environment variable for Airbus proxy")
    st.write('You might need to remove your environment variable called "HTTPS_PROXY" and "HTTP_PROXY". Use one of the command below:')
    st.code("""conda env config vars set HTTPS_PROXY=
set HTTPS_PROXY=""", language='SHELL')
