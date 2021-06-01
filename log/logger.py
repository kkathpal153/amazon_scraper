#!/usr/bin/env python
import logging

def get_logger(script_name):
    """
    It is used to monitor the erros and internal working of the applicaiton
    A custom logger is creater that displays timestamp, level_of_log and details in app.log

    Parameter:
    script_name - > The script name where it's object is created to diplay result in 
    
    Returns:
    An object of logger that can be used to log information in app.log
    """
    
    log_format = '%(asctime)s  %(name)8s  %(levelname)5s  %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=log_format,
                        filename='app.log',
                        filemode='a')

    return logging.getLogger(script_name)