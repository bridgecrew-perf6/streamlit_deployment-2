import streamlit as st
from multiapp import MultiApp
from apps import goal_and_installation, trouble_with_airbus_laptop, database, test_model, put_in_prod


if __name__ == '__main__':
    st.set_page_config(layout="wide",
                       page_title="Deployment tutorial",
                       page_icon="favicon.png")
    app = MultiApp()
    st.sidebar.image("logo_aqsone.png")
    # Add all your application here
    app.add_app("Goal of the workshop and installation", goal_and_installation.app)
    app.add_app("Download a model - With Airbus proxy", trouble_with_airbus_laptop.app)
    app.add_app("Test the model", test_model.app)
    app.add_app("Put in production", put_in_prod.app)
    app.add_app("Database", database.app)
    # The main app
    app.run()
    st.sidebar.markdown("[Link to the pandore article](https://sites.google.com/aqsone.com/pandore/mise-en-production/comment-publier-un-mod%C3%A8le-en-5min?authuser=1)")
    st.sidebar.markdown("[Link to streamlit cheatsheet and documentation](https://docs.streamlit.io/library/cheatsheet)")
    st.sidebar.markdown("[Fill mask with DistillBert](https://huggingface.co/distilbert-base-uncased)")
    st.sidebar.markdown("[Link to the Github repository](https://github.com/dauriacpaul/streamlit_deployment)")
