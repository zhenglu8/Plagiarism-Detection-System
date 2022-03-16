import pyrebase

#Configure and Connext to Firebase

firebaseConfig = {	'apiKey': "",
					'authDomain': "",
					'databaseURL': "",
					'projectId': "",
					'storageBucket': "",
					'messagingSenderId': "",
					'appId': "",
					'measurementId': ""}



firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#Login function

def login(email, password):
	login = auth.sign_in_with_email_and_password(email, password)
	return


#Signup Function

def signup(email, password):
	user = auth.create_user_with_email_and_password(email, password)
	return
