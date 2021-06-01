from requirements import requirements
from log import logger
from scrape import scraper
from links import linker

log = logger.get_logger('app.py')

def application():

    #checking the essential libraries
    try:
        
        requirements.require( requirement_file= 'requirements/requirements.txt')

        links_list = linker.links( links_file= 'links/links.txt')

    except Exception as e:
        log.error(e.args)
    
    #making a list of valid amazon links
    result_list = []
    for link in links_list:
        result_list.append(scraper.getPrice(link))
    
    print (result_list)

if (__name__ == "__main__"):
    application()