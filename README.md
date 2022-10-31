# merge-challenge

Some notebooks to play around with [data at the merge](https://esp.ethereum.foundation/merge-data-challenge).

Take a look at the [blog post](https://hackmd.io/@fmrmf/HyFXVQdVo) explaining the notebooks in detail.


## Setup

This repo uses [ApeWorX](https://github.com/ApeWorX/ape) for much of the data analysis. To start, clone the repo

```
$ git clone https://github.com/fmrmf/merge-challenge.git
$ cd merge-challenge
```

and install `ape` along with the plugins needed for this project

```
$ pipx install eth-ape
$ ape plugins install .
```

## Environment

You'll need to set environment variables for the network provider to work properly. An example `.env.example` file is included, which assumes using Alchemy as the network provider:

```
$ export WEB3_ALCHEMY_PROJECT_ID=MY_ALCHEMY_PROJECT_ID
$ export ETHERSCAN_TOKEN=MY_ETHERSCAN_TOKEN
```

Substitute `WEB3_ALCHEMY_PROJECT_ID` for another environment variable if using a different provider (e.g. [Infura](https://github.com/ApeWorX/ape-infura#quick-usage)).


## Running

To interact with all the Jupyter notebooks, run

```
$ ape notebook
```
