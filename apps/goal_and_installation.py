import streamlit as st
from streamlit import write


def app():
    st.header("Workshop put a model into prod")
    write(
        "The goal of this workshop is to present how to put a model into production. In addition to that, we will link our model to a database")
    write(
        "To do so, we will use streamlit and the streamlit Cloud feature which allows to have a private application hosted for free")
    st.subheader("Proposed model and task")
    st.markdown(
        "We propose to use an NLP model using Transformers. We have loaded ours with the [:hugging_face: Hugging Face "
        "library](https://huggingface.co/)")
    write(
        """We have used the DistillBERT model and perform the "fill-mask" task which consists in removing a word from a sentence and let the model fill the missing word""")
    st.markdown("If you wish, you are free to use another library or perform another [task](https://huggingface.co/docs/transformers/task_summary).")
    st.subheader("Required library")
    st.markdown("""
        If you want to use HuggingFace, you need the following library:
        * streamlit
        * pandas
        * PyTorch
        * transformers
        * google-cloud-firestore
    """)
    with open("requirements.txt", encoding="utf8", errors='ignore') as file:
        st.download_button("Download the requirements.txt",
                           data=file,
                           file_name="requirements.txt",
                           mime="text/plain")
    st.subheader("Time to try streamlit")
    st.markdown("To write your first streamlit app, you can refer to the [streamlit doc](https://docs.streamlit.io/library/cheatsheet) and the [pandore article](https://sites.google.com/aqsone.com/pandore/mise-en-production/comment-publier-un-mod%C3%A8le-en-5min?authuser=1#h.g1h7vmgivksr).")
    st.write("For this workshop, you will need the [text_input](https://docs.streamlit.io/library/api-reference/widgets/st.text_input) and [write](https://docs.streamlit.io/library/api-reference/write-magic/st.write) commands.")
    st.write("An example and the results of those commands is shown below:")
    with st.echo():
        title = st.text_input('Movie title', 'Life of Brian')
        st.write('The current movie title is', title)


if __name__ == '__main__':
    app()
