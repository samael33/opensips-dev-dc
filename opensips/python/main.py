""" Test Python script.

Called by OpenSIPS via python module
python module documentation: https://opensips.org/docs/modules/3.4.x/python.html

This module merges functionalities of:
 - Push Notifications
"""

import pn_client
from utils import get_logger, OPENSIPS_SUCCESS_CODE, OPENSIPS_ERROR_CODE

MODULE_NAME = 'python_opensips'
logger = get_logger(MODULE_NAME)



class PyOpensips:
    def __init__(self):
        logger.info("{}.__init__() called, id: {}".format(self.__class__.__name__, id(self)))
        self.pn = pn_client.mod_init()

        # PN methods
        self.pn_clean_contact = self.pn.handler_clean_contact
        self.pn_register_pn_token = self.pn.handler_register_pn_token
        self.pn_trigger_pn = self.pn.handler_trigger_pn
        self.pn_delete_token = self.pn.handler_delete_token


    def child_init(self, rank):
        """Executed by ython module when a new worker process (child) is initialized by Opensips."""
        logger.debug(f"{self.__class__.__name__}.child_init() called with rank {rank}, id {id(self)}")
        return OPENSIPS_SUCCESS_CODE


def mod_init():
    """ Executed by python module when it is initialized by OpenSIPS."""
    logger.debug(f"mod_init() called, returning PyOpensips script, dir {dir()}")
    return PyOpensips()
