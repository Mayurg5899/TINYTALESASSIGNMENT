# TINYTALESASSIGNMENT 
ASSIGNMENT FOR  TINYTALES BASED ON USE OF BACKEND,FRONTEND,GUI
ASSIGNMENT CONSISTS OF QUESTIONS or TASKS THAT NEED TO BE FOLLOWED BY OUR OBJECT CODE:
A.. A front end which accepts a number input N with a Submit button (extra points for building frontend in React or a HTML5 framework)

B. On entering a value and pressing submit, a request should be sent to the backend (backend can be in any technology, extra points for using nodejs)

C. From the backend, fetch a file hosted at http://terriblytinytales.com/test.txt

D. From the backend, return the top N most frequently occurring words in this file (do not use a ready made module for frequency computation)

E. Display the top N words and their frequency of occurrence in the frontend, in a tabular format

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# SOLUTION :
so our source code comprises of following things:
        ## 1.LANGUAGE USED :PYTHON ; ##
        ## 2.GUI LIBRARY USED : TKINTER(IN-BUILT GUI LIBRARY IN PYTHON ;##
        ## 3.DATABASE USED : SQLITE3 INBUILT DATABASE PACKAGE IN PYTHON ;##
        ## 4.SOURE CODE : THERE ARE TOTAL 2 FILES (1 FOR FRONTEND AND 1 FOR BACKEND ;##
        
# HOW DOES THIS PROJECT WORK
1.We have a frontend which consists:
                      A.LABEL("enter a number")
                      B.ENTRY("space for entering number queries you want to retrive")
                      C.LISTBOX("for showing the output")
                      
  ![](https://github.com/Mayurg5899/TINYTALESASSIGNMENT/blob/master/frontend.png)
  
 
 2.we have database named backend.sqlite where we have a table called WordsCount which we used to store the words in the textfile  " http://terriblytinytales.com/test.txt" along with their counts
 
 ![](https://github.com/Mayurg5899/TINYTALESASSIGNMENT/blob/master/2020-08-08%2017_47_18-Greenshotdatabase.png)
 
 3.now we have to retrive the top most frequent words from the database along with their count as the number entered by user in the entry box:
 
# a.TEST CASE 1:
      WHEN USER ENTER 4 IN THE ENTRY so RESULT RETRIVE TOP FOUR WORDS WITH MAXIMUM COUNTS from DATABASE
 
 ![](https://github.com/Mayurg5899/TINYTALESASSIGNMENT/blob/master/testcondition1.png)
 
# b.TEST CASE 2: 
    WHEN USER ENTER 6 IN THE ENTRY RESULT FETCHES TOP 6 WORDS WITH MAXIMUM COUNTS
 
 ![](https://github.com/Mayurg5899/TINYTALESASSIGNMENT/blob/master/testcondition2t.png)
 
 
 
 
 
 
           
