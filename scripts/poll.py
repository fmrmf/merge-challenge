import click

from ape import chain, networks


def main():
    """
    poll.py polls for new blocks from EL and saves them
    to a csv.
    """
    ecosystem_name = networks.provider.network.ecosystem.name
    network_name = networks.provider.network.name
    provider_name = networks.provider.name
    connection_name = f'{ecosystem_name}:{network_name}:{provider_name}'
    click.echo(f"You are connected to provider network {connection_name}.")

    # TODO: append rows of blocks and txs in each block to csvs
    # TODO: in case ppl would like real-time historical
    # TODO: charts (i.e. this runs, updates csv or
    # TODO: time series db, server displays)

    start_block_number = click.prompt(
        "Polling start block", type=int, default=-1)
    if start_block_number < 0:
        start_block_number = None  # default to current block

    click.echo("Polling for new blocks ...")
    for block in chain.blocks.poll_blocks(start_block=start_block_number):
        click.echo(f"Found new block. #: {block.number}")
        txs = block.transactions
        print('new block:', block)
        print('txs in new block:', txs)
