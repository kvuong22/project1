1. definitions are available in lab3_code.py, and/or what the relationship between lab3_code.py and si507_project1.py

lab3_code.py contains the parent class Currency and along with it the subclasses Dollar, Pound, and Yuan. The class Currency contains a conversion function that checks if the type of currency matches with one of the subclasses of Currency to convert the amount. Each of the subclasses contain a different rate that corresponds to the specific type of currency for the conversion. The class Bank has a deposit function which checks if the currency of the deposit amount matches with the bank's currency. If it does, the amount is deposited and noted confirmation of the transaction by the return statement, "successful deposit." If the currency does not match up with the bank's, a message indicating "ERROR: cannot deposit that currency," to notify the user the transaction was unsuccessful.

SI507_project1.py imports all of the code from lab3_code.py and utilizes the Flask module to use the code in a Flask application, viewable via web browser and can be tested through a web browser.


2. Makes clear what dependencies the project relies on, and/or tells the reader that you can install everything you need by using the included requirements.txt file.

3. Explains exactly how to run the Flask app, down to what to type in to your command prompt.
