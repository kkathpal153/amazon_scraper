#!/usr/bin/env python

#trying to install the essential libraries required by the project first
try:
    from requirements import requirements
    requirements.require( requirement_file= 'requirements/requirements.txt')
except:
    pass
finally:
    from log import logger
    from scrape import scraper
    from links import linker
    import pprint


#log object for application script
LOG = logger.get_logger('app.py')


def application():
    """ 
    I created this applicaiton as a personal project to monitor the prices of some amazon items that are in my bucket list
    It uses beautiful soup to download pages and validators to check links.

    Application is simple yet elegant as it automatically installs the required libraries and run the application

    This application runs in 3 steps
    Step 1: Required packages are installed if not present
    Step 2: The links provided by the user in links/links.txt files are verified for official amazon links
    Step 3: The Scraper takes the links list and extract the Names and Prices from amazon pages.

    Returns:

    List of each product information and prices. 
    """


    #checking the essential libraries
    try:
        #list of valid links
        links_list = linker.links( links_file= 'links/links.txt')
    except Exception as e:
        LOG.error(e.args)
    
    #making a list of valid amazon links
    result_list = []
    for link in links_list:
        result_list.append(scraper.getPrice(link))
    
    #returning the list of deatils from valid links
    return result_list


if (__name__ == "__main__"):

    result = application()
    print (result)