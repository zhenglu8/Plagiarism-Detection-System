import pyrebase
import os
from pysimilar import compare
from pysimilar import compare_documents
import pysimilar as py

##                   PYRECHECK CLASS                   ##
# Pyrecheck expects plaintext file extension types only #
##                                                     ##
class pyrecheck:
    # Configuration for Fireconfig and the app instance itself
    app = None
    firebaseConfig = None

    # Storage instance
    storage = None

    # File we're checking against the one we have to check 
    file_against = None
    file_check = None

    # The latest comparison check
    comparison_latest = None

    def __init__(self, file_check, firebaseConfig):
        self.file_check = file_check
        self.comparison_latest = 0
        self.firebaseConfig = firebaseConfig

    ## Connect to the firebase config ##
    def connect(self):
        self.app = pyrebase.initialize_app(self.firebaseConfig)
    
    ## Get the app instance ##
    def get_instance(self):
        return self.app
    
    ## Get the config instance ##
    def get_config(self):
        return self.firebaseConfig

    ## MANDATORY ##
    ## Connect to the storage ##
    def connect_storage(self):
        try:
            print("-- Trying to connect to the storage --")
            self.storage = self.app.storage()
            print("Connected to storage!")
        except Exception as e: 
            print("Please make sure you auth first using the config")
            print(e)

    ## OPTIONAL ##
    ## Connect to the database ##
    def connect_database(self):
        try:
            print("Trying to conenct to the database")
            self.database = self.app.database()
            print("Connected to the database!")
        except Exception as e:
            print("Please make sure you auth first using the config")
            print(e)

    ## Get a list of all the files checking against in the DB and compare the files ##
    def compare_against_files(self): 
        files_check = self.storage.list_files()
        
        try:
            for file in files_check:
                print(file.name)

                try:
                    if('.' not in file.name):
                        open(file.name + ".txt", 'a').close()
                        self.file_against = file.name + ".txt"
                    else:
                        open(file.name, 'a').close()
                        self.file_against = file.name

                    file.download_to_filename(self.file_against)

                except Exception: 
                    continue

                self.__compare_files()
                os.remove("./" + self.file_against)
        except Exception as e: 
            print(e)

    ## PRIVATE ##
    ## Compare files using pysimilar method compare ##
    def __compare_files(self):
        try:
            curr_check = compare(self.file_check, self.file_against, isfile=True)
            print(curr_check)
            if(curr_check > self.comparison_latest):
                self.comparison_latest = curr_check
        except Exception as e: 
            print(e)

    ## Return the internal result counter ##
    def return_results(self):
        return self.comparison_latest

###################################
### Example run using pyrecheck ###
###################################
# firebaseConfig = {'apiKey': "AIzaSyAEp8_HarY6xSVZEgiXiko67ntgVuCXmwg",
#                 'authDomain': "integrationproject-8160f.firebaseapp.com",
#                 'databaseURL': "https://integrationproject-8160f-default-rtdb.firebaseio.com/",
#                 'projectId': "integrationproject-8160f",
#                 'storageBucket': "integrationproject-8160f.appspot.com",
#                 'messagingSenderId': "1053011153629",
#                 'appId': "1:1053011153629:web:b1f1c1a15cb213c2f88134",
#                 'measurementId': "G-9T553ECDE0",
#                 'serviceAccount': "./integrationproject-8160f-9749c3e42fc7.json"}

## Running the module in order ## 
# Create object with the text file we're comparing against
# checking = pyrecheck("doc_test.txt", firebaseConfig)

# # Connect to firebase
# checking.connect()

# # DEBUG # 
# # Get the instance
# # Get the config 
# print(checking.get_instance())
# print(checking.get_config())

# # Connect to the storage
# # Connect to the database
# checking.connect_storage()
# # checking.connect_database()

# # Compare against all the files in the storage
# print("-- Check against database --")
# checking.compare_against_files()

# # Return the results 
# print(checking.return_results())
