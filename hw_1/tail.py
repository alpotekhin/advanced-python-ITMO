import click
import sys

def print_tail(file, lines=10):
    """Prints last N lines of a file"""
    with open(file, 'r') as f:
        content = f.readlines()
        for line in content[-lines:]:
            click.echo(line, nl=False)
    click.echo()

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def tail(files):
    """Python 'tail' utility implementation."""
    if not files:
        for line in sys.stdin.readlines()[-17:]:
            click.echo(line, nl=False)
    else:
        for file in files:
            if len(files) > 1:
                click.echo(f"==> {file} <==")
            print_tail(file)

if __name__ == "__main__":
    tail()
