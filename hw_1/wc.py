import click
import sys

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def wc(files):
    """Python version of the 'wc' utility implementation with output formatting similar to the original wc command."""
    total_lines = total_words = total_chars = 0

    def process_content(content, name=None):
        """Processes content and prints statistics with formatting similar to the original."""
        lines = content.count('\n')
        words = len(content.split())
        chars = len(content)
        # Format output, right-aligning numbers
        click.echo(f"{str(lines).rjust(8)}{str(words).rjust(8)}{str(chars).rjust(8)}" + (f" {name}" if name else ""))

        return lines, words, chars

    if files:
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
                lines, words, chars = process_content(content, file)
                total_lines += lines
                total_words += words
                total_chars += chars

        if len(files) > 1:
            click.echo(f"{str(total_lines).rjust(8)}{str(total_words).rjust(8)}{str(total_chars).rjust(8)} total")
    else:
        # Read from stdin if no files are provided
        content = click.get_text_stream('stdin').read()
        process_content(content)

if __name__ == "__main__":
    wc()
