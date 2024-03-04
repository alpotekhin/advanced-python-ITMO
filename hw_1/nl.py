import click
import sys

@click.command()
@click.argument('file', type=click.File('r'), required=False)
def number_lines(file):
    """
    Print numbered lines from a file or stdin.
    """
    if file:
        for i, line in enumerate(file, 1):
            click.echo(f"{i}\t{line}", nl=False)
    else:
        # Read from stdin if no file path is provided
        click.echo("Enter text (Ctrl-Z to stop):", err=True)
        for i, line in enumerate(sys.stdin, 1):
            click.echo(f"{i}\t{line}", nl=False)

if __name__ == "__main__":
    number_lines()
