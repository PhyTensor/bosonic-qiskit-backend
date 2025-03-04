import logging
import os
import sys


def setup_global_logging(log_level=logging.INFO, log_filename='bosonic.log'):
    """
    Set up global logging.

    This function configures the root logger to log messages at the
    specified log_level. Log messages are sent to both stdout and a file
    located at the package root directory.

    Args:
        log_level (int): Logging level (e.g. logging.DEBUG, logging.INFO).
        log_filename (str): Name of the log file to create.
    """
    logger = logging.getLogger()  # get the root logger
    logger.setLevel(log_level)

    # Remove any existing handlers (for re-import scenarios)
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create a formatter for the logs
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Create and add StreamHandler for stdout
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Determine absolute path for the log file in the package root
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(base_dir, log_filename)

    # Create and add FileHandler
    file_handler = logging.FileHandler(file_path, mode='a', encoding='utf-8')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# Automatically configure logging when the module is imported
setup_global_logging()

