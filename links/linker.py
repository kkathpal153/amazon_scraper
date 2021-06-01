#!/usr/bin/env python
import validators
from log import logger

#Creating log object for linkey.py
LOG = logger.get_logger('linker.py')


def links(links_file):

    """
    This function returns the list of all the valid links present in the links_file

    PARAMETERS:
    links_file -> location of the file containing links in the directory

    Returns:
    Return a list of valid links.
    """

    links = []

    #opening file containing list of user given links 
    #and making a valid links list out of it
    try:
        with open(links_file, 'r') as file:
            for value in file:
                #if the link is valid amazon link append it to links list
                if(validator(value[:-1])):    
                    LOG.info("Valid URL " + value[:-1])
                    links.append(value[:-1])
                else:
                    LOG.error("Invalid URL : " + value[:-1] )
    except IOError as exception:
        LOG.error(str(exception))
    finally:
        #returing list of valid links
        return links



#function to check if the links are valid or not
def validator(link):
    """
    Checks for validity of the links using validator package.

    Parameters:
    links -> Accepts the string containing link from links file

    Return:
    True if the url is a valid amazon url
    False otherwise
    """
    result = False
    try :
        if(validators.url(link)):
            if( link.find('www.amazon.') != -1):
                result = True
    except Exception as e:
        LOG.error(e.args)
    finally:
        return result
