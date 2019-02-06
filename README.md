# **README**

## **Definitions for Functions in lab3_code.py**
lab3_code.py contains the parent class Currency and along with it the subclasses Dollar, Pound, and Yuan. The class Currency contains a conversion function that checks if the type of currency matches with one of the subclasses of Currency to convert the amount. Each of the subclasses contain a different rate that corresponds to the specific type of currency for the conversion. The class Bank has a deposit function which checks if the currency of the deposit amount matches with the bank's currency. If it does, the amount is deposited and noted confirmation of the transaction by the return statement, "successful deposit." If the currency does not match up with the bank's, a message indicating "ERROR: cannot deposit that currency," to notify the user the transaction was unsuccessful.

## **Relationship between lab3_code.py and SI507_project1.py**
SI507_project1.py imports all of the code from lab3_code.py and utilizes the Flask module to use the code in a Flask application, viewable via web browser and can be tested through a web browser.



## **Project Dependencies**

This project requires installation of what is listed in the requirements.txt file to run the project.



## **Running Flask Application**

To run the Flask application, in the command prompt, run 'python SI507_project1.py runserver'. Access the webpage either by using 1) the generated URL in the command prompt or by using the URL link 2) http://localhost:5000 and paste it into the browser. The home page should have a message saying, "Welcome to the banking application!"

### **Accessing Routes**
To access the route to the bank name, edit the URL parameters in the browser to include '/bank/*name*' and input the name of the bank to get the message "Welcome to 'name'." To access the route for the amount of the currency (Dollar, Pound, or Yuan), edit the URL parameters in the browser to include '/*currency*/*amt*' and input one of the three currencies (Dollar, Pound, Yuan) in the *currency* parameter and an integer where *amt* is. The message will print the amount and the currency input. Lastly, to access the route for the bank, currency, and amount, edit the URL parameters in the browser to include '/bank/*name*/*currency*/*value*' and input the bank's name for *name*, type of currency for *currency*, and an integer for the *value*. If the currency input is Dollar, Pound, or Yuan, you will get the message: "*name* Bank holds the *currency matching Dollar, Pound, or Yuan* currency and currently holds *integer value* of *currency*." If the currency input does not match any of the three subclasses defined in lab3_code.py, you will get the message: "INVALID URL inputs for bank."
