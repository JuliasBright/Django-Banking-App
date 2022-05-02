<h1>Project Structure</h1>

- Banking App
    - Bank Accounts
        - Hold all of the users accounts
    - Bank Admin
        - Responsible for the csv files and admin opreations
    - Bank App
        - Core application
    - Bank Users
        - Hold all users registered for the bank
    - Bank Transactions
        - Holds and record all accounts transactions
    


<h2>Running the Project</h2>

-  Navigate to the root of the app which has both manage.py and requirement.txt.
- Install all the application dependancies by running <i>pip install -r requirments.txt</i>
- Start the application by running the command <i>python manage.py runserver</i>
- Navigate to the admin. To create transactions and users using the Ui <http://127.0.0.1:8000/admin/>
- You can now be able to see and curl all the data and users from the local host.
 

### Project Credentials
- Superuser account::
- Username:: bankingapp
- Emailadress: bankingapp@example.com
- Password: bankingapp123456@


<h3>Running Test</h3>

To run the whole project test cases typr the command
- python manage.py test --parallel
- Test Bank users
    - You can run the following 
        - python manage.py test bankusers.tests.ModelsTest.bankUser_test
- Test Bank Accounts
    - You can run the following
        - python manage.py test bankaccounts.tests.ModelTests.Account
- Test Bank Admin
    - You can run the following
        - python manage.py test bankadmin.tests  



### we can provide the output option to save to a file:
- curl -o out.json http://127.0.0.1:8000/
- curl -o out.json http://127.0.0.1:8000/rest_apis/bankaccounts   
- curl -o out.json http://127.0.0.1:8000/rest_apis/bankusers  
- curl -o out.json http://127.0.0.1:8000/rest_apis/banktransactions  

### Since we have the verbose mode on, we get a little more information along with the response body:
- curl -v http://127.0.0.1:8000/rest_apis/banktransactions
- curl -v http://127.0.0.1:8000/

### Alternatively, we can post a file containing the request body to the data option like this
- curl -d 'id=5445&user_name=test' http://127.0.0.1:8000/rest_apis/bankusers
- curl -d @request.json -H "Content-Type: application/json" 
  http://127.0.0.1:8000/rest_apis/bankaccounts 


### we specify that we want to use DELETE by using the -X option:
- curl -X DELETE http://127.0.0.1:8000/rest_apis/bankusers/test/5445

