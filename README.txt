AMAZON Scraper
This is a fun project I created monitor changes in prduct prices of some Amazon Items.
Application first installs required packages automatically and then validates the links present in links.tst file
and then scrapes links read from a file. Every error or info is logged into app.log

Instructions:
Edit the amazon product links in links/links.txt file.

  amazon_scraper
    |
    |-links
       |-links.txt
       |-linker.py
    |-requirements
    |-scrape
    |-logger
    |-app.py
    |-app.log
    
Note: To monitor what's happening in the application open app.log
