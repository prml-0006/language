"""Module steps.py"""
import logging

import pandas as pd

import src.elements.variable
import src.models.structures


class Steps:
    """
    Steps
    """

    def __init__(self, enumerator: dict, archetype: dict,
                 training: pd.DataFrame, validating: pd.DataFrame):
        """

        :param enumerator:
        :param archetype:
        :param training:
        :param validating:
        """

        # Inputs
        self.__enumerator = enumerator
        self.__archetype = archetype

        # A set of values for machine learning model development
        self.__variable = src.elements.variable.Variable()
        self.__variable = self.__variable._replace(EPOCHS=2, TRAIN_BATCH_SIZE=16, VALID_BATCH_SIZE=16)

        # Instances
        self.__structures = src.models.structures.Structures(
            enumerator=self.__enumerator, variable=self.__variable,
            training=training, validating=validating)

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self):
        """

        :return:
        """

        training = self.__structures.training()
        validating = self.__structures.validating()
