# logger.py
import logging


def setup_logger():
    logger = logging.getLogger("DebateLogger")
    logger.setLevel(logging.INFO)

    # Create file handler
    fh = logging.FileHandler("debate_log.txt")
    fh.setLevel(logging.INFO)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(fh)

    return logger
