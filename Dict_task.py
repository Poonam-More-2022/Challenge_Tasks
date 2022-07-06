''' Dictionary Tasks:
#1. Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2 level nesting it should work.
#2. Try to find out number of keys in dict element from given dictionary
#3.Try to create a dictionary containing squares and cubes for given numbers
'''

import logging
logging.basicConfig(filename="dict_test.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class dict_task:

#1 . Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2 level nesting it should work.
    def dict_values(self,D):
        ''' This function returns the list of all values present in dictionary'''
        try:
            logging.info("The dictionary Entered by user : %s", D)
            l = []
            for i in D.values():
                if type(i) != dict:
                    l.append(i)
                else:
                    for j in dict_task.dict_values(self,i):       #Using  reccursion
                        l.append(j)
            logging.info("The list of all values present in dictionary : %s", l)
            return l
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e


#2. Try to find out number of keys in dict element from given dictionary
    def no_of_keys(self,D):
        '''This function gives the number of keys in dict element from given dictionary'''
        try:
            logging.info("The dictionary Entered by user : %s", D)
            if type(D) == dict:
                logging.info("Number of keys in dictionary element from given dictionary : %s", len(D))
                return len(D)
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e

#3.Try to create a dictionary containing squares and cubes for given numbers
    def sq_cube(self, *x):
        """ Creates a dictionary containing squares and cubes for given numbers """
        try:
            logging.info("The Numbers Entered by user : %s", x)
            D={"Square":[i*i for i in x], "Cube":[i**3 for i in x]}
            logging.info("Dictionary containing squares and cubes for given numbers : %s", D)
            return D
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e
