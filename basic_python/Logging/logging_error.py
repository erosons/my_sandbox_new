import logging
import string

"""
- logging.debug("debug-level message) => Diagnostic informarion useful for debugging
- logging.info("infolevel message)  => GenerL informaation about program execution result
- logging.warning("warning-level message) => Something unexpected or an approaching problem e.g out of storage or failed server communication
- logging.error("error-level message) => Unable to perform a specific opearation due to problem
- logging.critical("critical-level message) => Program may not be able continue , serious error

Note only warning, error, critical are displayed by default to make other logging show we have to setup configuration
"""

extData = {
    "user": "samson@gmail.com"
}

def anothelog():
    logging.debug("This is another log message caller", extra=extData)


def main():

    ##### APPROACH 1 : Customizing your logging and writing to file
    formstr = "User:%(user)s %(asctime)s : %(name)s:%(levelname)s:%(message)s:%(funcName)s Line:%(lineno)d"
    datestr = "%m/%d/%Y %I:%M:%S %p"

    logging.basicConfig(level=logging.DEBUG,
                        filename="myPythonprojects/MainDirectory/tutorial/log_output.log",
                        filemode="w", format=formstr, datefmt=datestr)

    # TODO  Try out each of the loggings
    logging.debug("debug-level message", extra=extData)
    logging.info("infolevel message", extra=extData)
    logging.warning("warning-level message", extra=extData)
    logging.error("error-level message", extra=extData)
    logging.critical("critical-level message", extra=extData)

   # logging.info("Here's {} varable and an int:".format("string", 10))


###### APPROACH 2: Customizing your logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


###### APPROACH 3: Customizing your logging
# Basic configuration for the root logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Create a logger instance (this uses the root logger with basicConfig settings)
logger = logging.getLogger()

# Example usage
logger.info("This is an info message")


if __name__ == "__main__":
    main()
    anothelog()
