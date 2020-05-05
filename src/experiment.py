import getpass
from sacred import Experiment


ex = Experiment("MNIST")
# TODO: Add MongoDB
# TODO: Add SlackBot

@ex.config
def default():
    username = getpass.getuser()
    # TODO: Add configuration


@ex.automain
def main():
    # TODO: Train and validate model
    # TODO: Add logging
    # TODO: Add metrics
    # TODO: Add a way to download the dataset
    # TODO: Improve model
    pass