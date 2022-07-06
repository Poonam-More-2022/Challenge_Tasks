''' Set tasks:
#1. Try to extract all set entities from given list
'''
import logging
logging.basicConfig(filename="set_test.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class Set_task:

#1. Try to extract all set entities from given list
    def extract_set(self,L):
        ''' This function extracts all set entities from given list'''
        try:
            logging.info("List entered by user : %s", L)
            for i in L:
                if type(i)==set:
                    return i
        except Exception as e:
            logging.error(e)
            logging.exception(e)
            return e