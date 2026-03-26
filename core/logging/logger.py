import logging
import os
from datetime import datetime


def get_logger(agent_name: str):
    log_dir = os.getenv("LOG_DIR", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file_path = os.path.join(log_dir, f"{agent_name}.log")

    logger = logging.getLogger(agent_name)
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    logger.setLevel(level)

    # Prevent duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger