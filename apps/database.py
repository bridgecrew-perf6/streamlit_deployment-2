import pandas as pd
import streamlit as st
from streamlit import write
from google.cloud import firestore


def app():
    st.subheader("A possible database: Firestore")
    st.markdown("To connect our Firestore database to Streamlit, we've used this [tutorial](https://blog.streamlit.io/streamlit-firestore/#part-2-setting-up-firestore). Since the tutorial is great, you can follow it. **The main issue with firebase is that we don't know how to use it under an Airbus proxy. Hence, you might have to test directly in production.**")
    st.subheader("Link firestore to streamlit")
    st.write("If it's not already done, don't forget to set up your firebase account. You can do it by following the tutorial or with this [link](https://console.firebase.google.com/)")
    st.write('To link streamlit to firestore, you need to generate a JSON key. You can do it by following the video below')
    st.video("generate_firebase_key.webm")
    st.subheader("Streamlit secrets")
    st.write("In order to pass your JSON key to your app without publishing your private key on github, we will use Streamlit's secrets and a secrets.toml file when you work locally.")
    st.markdown("1. Create a folder .streamlit in the directory of your app")
    st.markdown("2. Copy the information of the JSON key in the .streamlit/secret.toml file. It should look like this:")
    st.code("""[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx" """, language="TOML")
    st.markdown("3. Link the code to your secrets.toml. Simply use the following command:")
    st.code("""from google.cloud import firestore
db = firestore.Client.from_service_account_info(st.secrets["gcp_service_account"])""")
    st.markdown("4. Now the credentials are set in local. You can now add them to the streamlit's secrets like on the following video:")
    st.video("streamlit_secrets.webm")
    st.subheader("Get and post data to firestore")
    st.markdown("A tutorial is shown in [this part of the pandore article](https://sites.google.com/aqsone.com/pandore/mise-en-production/comment-publier-un-mod%C3%A8le-en-5min?authuser=1#h.fak2rfthj7ad)")
    st.write("The documentation for getting and posting data can be found at those links:")
    st.markdown("""
    * Get: https://firebase.google.com/docs/firestore/query-data/get-data
    * Post: https://firebase.google.com/docs/firestore/manage-data/add-data
    """)
    st.write("You will at least need to create a firestore database and a collection for this database. You can do it by following the video below:")
    st.video("create_collection.webm")
    st.subheader("Write an element in the database")
    st.markdown("You can either store automatically the results or use a button with [st.button](https://docs.streamlit.io/library/api-reference/widgets/st.button)")
    st.write('In the code bellow, I store the results in my collection "posts", the name of the document is the "sentence" given by the user and we pass a dictionnary containg the data.')
    st.code("""    if st.button("Store result in the database"):
db = firestore.Client.from_service_account_info(st.secrets["gcp_service_account"])
data = {
    u"table_results": result
}
db.collection("posts").document(sentence).set(data)""")

    st.subheader("Get an element from the database")

    st.write("To get data from the database, you can collect all the information stored")
    st.write("Then propose to the user to choose one of the elements stored (the selectbox below)")
    st.write("Finally get the data for the element choose by the user")
    st.code("""
        db = firestore.Client.from_service_account_info(st.secrets["gcp_service_account"])
docs = db.collection(u'posts').stream()
sentences = []
for doc in docs:
    sentences.append(doc.id)
selected_sentence = st.selectbox("Select a stored sentence to look at the result", sentences)
table = db.collection(u'posts').document(selected_sentence).get().to_dict()["table_results"]
write(pd.DataFrame(table))
    """)

    st.subheader("Explore stored results")
    db = firestore.Client.from_service_account_info(st.secrets["gcp_service_account"])
    docs = db.collection(u'posts').stream()
    sentences = []
    for doc in docs:
        sentences.append(doc.id)
    selected_sentence = st.selectbox("Select a stored sentence to look at the result", sentences)
    table = db.collection(u'posts').document(selected_sentence).get().to_dict()["table_results"]
    write(pd.DataFrame(table))


if __name__ == '__main__':
    app()
