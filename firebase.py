import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('yomama-a2c9a-firebase-adminsdk-8em0r-727ed5b4e4.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()



doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "chris", "last": "jo", "born": 1975})
