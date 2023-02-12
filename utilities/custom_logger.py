# import libraries
import logging
import inspect

class LogGenerator:

    @staticmethod
    def log_gen():
        
        logging.basicConfig(filename="A:/AutomationProjects_python/yourstore/logs/eshop.log",
                            level=logging.INFO,force=True, 
                            format="%(asctime)s: %(levelname)s: %(name)s: %("
                                                                  "funcName)s(): %(message)s:",
                            datefmt="%d-%b-%Y %H:%M:%S")
        
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        return logger