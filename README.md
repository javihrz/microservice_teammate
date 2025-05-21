Request data:

For the implementation of this microservice, requesting data means requesting to log a new savings goal. To request data from the microservice (named microservice_a.py):
  •	The Python file must be run in its own terminal.
  •	Contain a text file to serve as the communication pipeline (comm_pipe.txt, in this example).
  •	Contain a text file to serve as the savings goal logging file (savings_log.txt).

The Python file will loop until the communication pipeline text file has a valid number in the form of a string value. The (stringed) number must be a positive float value (ex: 10.00) or a positive integer value (ex: 50).
Once it detects a string value, it will save it as a variable and then clear the communication pipeline text file.


Receive data:

For the implementation of this microservice, receiving data means amending the savings goal logging file, and viewing the changes on the file itself. To receive data from the microservice (named microservice_a.py):
  •	The Python file must still be run in its own terminal.
  •	Contain a text file to serve as the communication pipeline (comm_pipe.txt, in this example).
  •	Contain a text file to serve as the savings goal logging file (savings_log.txt).

Once the microservice saves the string value from the communication pipeline file, it will also save in a variable the last logged goal from the savings goal logging file. After some numeric addition and string formatting, the new goal is amended to the savings goal logging file. After the savings goal logging file is amended, the microservice starts the loop over again. The user will be able to open the savings goal logging file and see that the new goal was logged in a new line (very last line in file).
