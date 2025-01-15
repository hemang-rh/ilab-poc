# from docling.document_converter import DocumentConverter


# def main():
#     source = "https://arxiv.org/pdf/2408.09869"
#     converter = DocumentConverter()
#     doc = converter.convert(source)
#     print(doc.document.export_to_markdown())

import click
import logging
from rich.console import Console
from .config import setup_logging
from .commands.convertdoc import convertdoc, convertdocs

console = Console()
logger = logging.getLogger('ilab_poc')


def init_app(log_level):
    setup_logging(log_level)
    logger.debug("Application initialized with log level: %s", log_level)


@click.group()
@click.option('--log-level',
              type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR'],
              case_sensitive=False),
              default='INFO',
              help='Set the logging level')
def cli(log_level):
    """Simple CLI application with Click and logging"""
    init_app(getattr(logging, log_level.upper()))


cli.add_command(convertdoc)
cli.add_command(convertdocs)

if __name__ == "__main__":
    cli()
