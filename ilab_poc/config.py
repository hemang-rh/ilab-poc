import logging
import logging.config
import os
from pathlib import Path
from rich.logging import RichHandler
from rich.console import Console


def setup_logging(log_level=logging.INFO):
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    console = Console()
    
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'rich': {
                'format': '%(message)s',
            },
            'file': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'rich': {
                'class': 'rich.logging.RichHandler',
                'level': 'INFO',
                'formatter': 'rich',
                'rich_tracebacks': True,
                'console': console,
                'show_time': True,
                'show_level': True,
                'show_path': False,
            },
            'file': {
                'level': 'DEBUG',
                'formatter': 'file',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join('logs', 'app.log'),
                'maxBytes': 10485760,  # 10MB
                'backupCount': 5
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['rich', 'file'],
                'level': 'INFO',
                'propagate': True
            },
            'simple_cli': {
                'handlers': ['rich', 'file'],
                'level': log_level,
                'propagate': False
            },
        }
    }

    logging.config.dictConfig(logging_config)
