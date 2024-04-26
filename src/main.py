import logging
import os
import sys

import pandas as pd
import torch

def main():

    logger: logging.Logger = logging.getLogger(__name__)

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    logger.info(msg=device)

    src.data.fundamentals.Fundamentals().exc()
    # logger.info(msg=data.head())
    # data.info()
    
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Modules
    import src.data.fundamentals
    import src.functions.cache


    main()