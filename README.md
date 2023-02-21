# final_library_project
All Files of Jhon Bryce 7732/3 Library Project - by Omer 

This project spanning 2 weeks
includes multiple files:
  1) front end file - the __main__ file of the projects creating all the menues and everything
  2) library file - the "last line: the file taking all the seperate functions and classes and binding them together to all the major functions
  3) 3 JSON log files - customers, books, log - contain all the respective information - about the books and thier details, the customers and thier information, and a log of all loans and returnes
    *currently this file contains some sample information
  4) logger file - the "work horse" of my project - contains almost all of the functions that interact with the log files - all three of them.
  5) loan file - contains the loan class and all its respective functions
  6) customer file - contains the customer class and all its functions - also contains the writing to customer log function
  7) book file - contains the book class and the functions, also has the writing to books file function 
  8) dates file - containing all functions regarding dates and datetime - taught me alot on how to use the module and interact with time in python
  9) address file - contains a simple class and some functions to interact with an effective address field for the customer class

languages used: python

pycharm plugins used: Sourcery - advices to make the code cleared and more effective 

modules used: datetime, json, pprint, fuzzywuzzy, python-Levenshtein (for optimizing fuzzywuzzy)

files format: JSON

important notes:
1) using inside your computer CMD panel, or pycharm Terminal (if set to default computer CMD terminal):

   PIP INTALL FUZZYWUZZY,
   
   PIP INSTALL Levenshtein - if it doesnt work try PIP INSTALL python-Levenstein
   
   or manually installing from pycharm install the package to be able to use the program
   
   
2) due to a problem with debugging of strptime in my pycharm, i used string iteration to handle dates and such - i know its not a real solution, but i have kept all my original datetime code for comparison


and thats it,

this project was definitely a challenge, taking alot of time, quite a lot of sweat, a little bit of tears and many long nights coding,

this project taught me alot and exposed me to new modules, functions, methods, quite abit of bugs but was overall a great learning opportunity. 

hope everything works and comes out okay.

Omer


thanks to this site for directing me to fuzzy wuzzy and python levenshtein
https://towardsdatascience.com/string-comparison-is-easy-with-fuzzywuzzy-library-611cc1888d97
