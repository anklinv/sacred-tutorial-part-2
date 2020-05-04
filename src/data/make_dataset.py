# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
import torchvision


@click.command()
@click.argument('output_filepath', type=click.Path(), default='../../data')
def main(output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    torchvision.datasets.MNIST(output_filepath, train=True, download=True)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
