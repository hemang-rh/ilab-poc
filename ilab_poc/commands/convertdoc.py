import click
import logging
from rich.console import Console
from docling.document_converter import DocumentConverter
from ilab_poc.utils import write_data_to_file
from pathlib import Path

console = Console()
logger = logging.getLogger('ilab_poc')


@click.command()
@click.argument('filepath')
def convertdoc(filepath):
    logger.info(f"Executing convertdoc command for name: {filepath}")
    try:
        source = filepath
        doc_converter = DocumentConverter()
        conv_result = doc_converter.convert(source)
        doc_filename = conv_result.input.file.stem
        output_file = f"{doc_filename}.md"
        write_data_to_file(output_file, conv_result.document.export_to_markdown())
    except Exception as e:
        logger.error("Error in hello command", exc_info=True)
        raise click.ClickException("Failed to execute hello command") from e


@click.command()
@click.option('--inputdir', '-i', required=True, 
              type=click.Path(exists=True, file_okay=False, dir_okay=True,
                              readable=True, path_type=str))
@click.option('--outputdir', '-o', required=False, 
              type=click.Path(file_okay=False, dir_okay=True,
                              writable=True, path_type=str))
def convertdocs(inputdir: Path, outputdir=None):
    logger.info(f"Executing convertdocs command for all files in inputdir: {inputdir}")
    try:
        files_to_convert = list(Path(inputdir).rglob('*.pdf'))
        doc_converter = DocumentConverter()
        for file in files_to_convert:
            conv_result = doc_converter.convert(file)
            doc_filename = conv_result.input.file.stem
            if outputdir:
                output_file = Path(outputdir) / f"{doc_filename}.md"
            else:
                output_file = file.parent / f"{doc_filename}.md"
            write_data_to_file(output_file, conv_result.document.export_to_markdown())
    except Exception as e:
        logger.error("Error in convertdocs command", exc_info=True)
        raise click.ClickException("Failed to execute convertdocs command") from e
