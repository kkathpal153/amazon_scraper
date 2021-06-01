#!/usr/bin/env python
"""Helps in installing the missing packages in your environment

    This script helps installing packages using PIP and requirements.txt
    It reads the packages names from requirements.txt and install using subprocess
    and sys packages.
"""

import subprocess
import sys
from log import logger


def require(requirement_file):
    LOG =  logger.get_logger('requirements.py')
    cmd_command =  [ 'pip  install  -r ', requirement_file]
    try:
        result = subprocess.Popen([sys.executable, "-m", cmd_command], stdout=subprocess.DEVNULL, stderr = subprocess.PIPE)
        process_output , process_error =  result.communicate()
        if process_error:     
            if (process_error.decode("utf-8").startswith("WARNING: ") ):
                 LOG.info(process_error)
            else:
                LOG.error(process_error)
        if process_output:
            LOG.info(process_output)

    except OSError as e:
           LOG.error(e.args)
           raise e
    except Exception as e:
        raise e
