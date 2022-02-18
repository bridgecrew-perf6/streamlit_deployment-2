import pandas as pd
import streamlit as st
from transformers import pipeline
from google.cloud import firestore


def app():
    st.write("For Airbus laptop, you need to replace the first line of the code by this line:")
    st.code("unmasker = pipeline('fill-mask', model='./distilbert-base-uncased')", language="python")

    st.subheader("Let's try the model!")
    with st.echo():
        from transformers import pipeline
        unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
        sentence = st.text_input('Fill in the sentence you want to try then press enter:', 'Data science is [MASK].')
        if "[MASK]" in sentence:
            result = unmasker(sentence)
            st.write(pd.DataFrame(result))
        else:
            st.warning("The sentence needs to contains [MASK]")

    if st.button("Store result in the database"):
        db = firestore.Client.from_service_account_info(st.secrets["gcp_service_account"])
        data = {
            u"table_results": result
        }
        db.collection("posts").document(sentence).set(data)


if __name__ == '__main__':
    app()
