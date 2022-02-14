import streamlit as st


def app():
    st.header("Time to put in prod")
    st.markdown("""
        This procedure is done in 3 steps:
        * Put your code into github (your personal repo, not the aqsone repository). Make sure to add the requirement**s**.txt with this exact spelling.
        * Create a [Streamlit cloud](https://share.streamlit.io/) account
        * Follow the instructions provided by Streamlit or the step shown in the video below
    """)
    st.video("https://youtu.be/czWaLgF9sA0")
    st.success("Congrats, your app is now online")

    st.info("From now, if you prefer, you can make the modifications directly on the github platform")
    st.write("NB: The free version of Streamlit allows you to have 1 private app")


if __name__ == '__main__':
    app()
