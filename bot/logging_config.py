import logging
import os

def setup_logger():
    # Create logger
    logger = logging.getLogger('trading_bot')
    logger.setLevel(logging.DEBUG)

    # Create file handler for logging to a file
    log_file = 'bot.log'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Create console handler for less noisy CLI output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)

    # Create formatters and add them to handlers
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
