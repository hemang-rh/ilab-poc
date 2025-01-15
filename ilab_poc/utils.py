import logging
from rich.console import Console

console = Console()
logger = logging.getLogger('ilab_poc')


def write_data_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        logger.info(f"Data successfully written to {file_path}")
    except Exception as e:
        logger.error(f"Failed to write data to file {file_path}: {e}")
        console.print(f"[bold red]Error:[/bold red] Failed to write data to {file_path}")
