#!/usr/bin/env python
"""Reads new links and old links in the txt file.

    This script helps in reading the links.txt file and returns
    a Valid amazon links.
"""

import validators
from log import logger

log = logger.get_logger('linker.py')

def links(links_file):
    links = []

    #opening file containing list of user given links 
    #and making a valid links list out of it
    try:
        with open(links_file, 'r') as file:
            for value in file:
                #if the link is valid amazon link append it to links list
                if(validator(value[:-1])):    
                    log.info("Valid URL " + value[:-1])
                    links.append(value[:-1])
                else:
                    log.error("Invalid URL : " + value[:-1] )
    except IOError as exception:
        log.error(str(exception))
    finally:
        return links



#function to check if the links are valid or not
def validator( link):
    result = False
    try :
        if(validators.url(link)):
            if( link.find('www.amazon.') != -1):
                result = True
    except Exception as e:
        log.error(e.args)
    finally:
        return result
