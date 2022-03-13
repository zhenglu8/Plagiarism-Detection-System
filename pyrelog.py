import pyrebase

#Configure and Connext to Firebase

firebaseConfig = {	'apiKey': "AIzaSyDL5bjW_xU5bfw6P2pBgwOHNo_h6dzeKnQ",
					'authDomain': "logintest-985f5.firebaseapp.com",
					'databaseURL': "https://logintest-985f5.firebaseio.com",
					'projectId': "logintest-985f5",
					'storageBucket': "logintest-985f5.appspot.com",
					'messagingSenderId': "732647019366",
					'appId': "1:732647019366:web:b6f9c7cc53378d6929aea7",
					'measurementId': "G-24Z8N5WV8J"}



firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#Login function

def test():
	print("test success")
	return

def login(email, password):
	login = auth.sign_in_with_email_and_password(email, password)
	return


#Signup Function

def signup(email, password):
	user = auth.create_user_with_email_and_password(email, password)
	return
