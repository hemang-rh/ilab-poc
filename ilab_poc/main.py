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

console = Console()
logger = logging.getLogger('simple_cli')


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


@cli.command()
@click.argument('name')
@click.option('--count', '-c', default=1, help='Number of times to greet')
def hello(name, count):
    """Say hello to someone multiple times"""
    logger.info("Executing hello command for name: %s with count: %d", name, count)
    try:
        for i in range(count):
            logger.debug("Printing greeting %d of %d", i + 1, count)
            console.print(f"Hello [blue]{name}[/blue]! 👋")
    except Exception as e:
        logger.error("Error in hello command", exc_info=True)
        raise click.ClickException("Failed to execute hello command") from e


if __name__ == "__main__":
    cli()
