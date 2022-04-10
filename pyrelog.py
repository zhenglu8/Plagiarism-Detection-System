import pyrebase

# Configure and Connext to Firebase

firebaseConfig = {'apiKey': "AIzaSyAEp8_HarY6xSVZEgiXiko67ntgVuCXmwg",
                  'authDomain': "integrationproject-8160f.firebaseapp.com",
                  'databaseURL': "https://integrationproject-8160f-default-rtdb.firebaseio.com",
                  'projectId': "integrationproject-8160f",
                  'storageBucket': "integrationproject-8160f.appspot.com",
                  'messagingSenderId': "1053011153629",
                  'appId': "1:1053011153629:web:b1f1c1a15cb213c2f88134",
                  'measurementId': "G-9T553ECDE0",
                  'serviceAccount': "./serviceaccountforalgorithm.json"}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Login function


def login(email, password):
    login = auth.sign_in_with_email_and_password(email, password)
    return


# Signup Function

def signup(email, password):
    user = auth.create_user_with_email_and_password(email, password)
    return
