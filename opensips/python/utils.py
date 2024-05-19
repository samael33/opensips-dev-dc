import logging
import logging.handlers

OPENSIPS_SUCCESS_CODE = 1
OPENSIPS_ERROR_CODE = -1

SIP_AUTH_SUCCESS_CODE = 200
SIP_AUTH_ERROR_CODE = 403

MAX_LOG_SIZE_BYTES = 10000000
LOG_FILE_BACKUP_COUNT = 10


def get_logger(module_name, debug_level = logging.DEBUG):
    logger = logging.getLogger(module_name)
    logger.setLevel(debug_level)
    fh = logging.handlers.RotatingFileHandler(
        '/var/log/' + module_name + '.log',
        mode='a',
        maxBytes=MAX_LOG_SIZE_BYTES,
        backupCount=LOG_FILE_BACKUP_COUNT
    )
    fh.setLevel(debug_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
