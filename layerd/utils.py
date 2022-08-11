"""
Layerd. Inspect Lambda Layers.
"""

import os
import sys

_flag_add_region = str(True).lower() in os.environ.get('LAYERD_REGION', '').lower()
_flag_parent_dir = os.environ.get('LAYERD_PARENT_DIR', '.')


def _stdout_del_last_row(
    width: int = os.get_terminal_size(0)[0],
) -> None:
    print(('\r') + (' ' * int(width)) + ('\r') , end='\r', flush=True)


def _progress_bar(
    current_iter: int,
    total_iter: int,
    message: str = None,
    width: int = os.get_terminal_size(0)[0] // 2,
) -> None:
    """
    format of done_z and done_x to be perceived as that of
    Statistic's Normal Distribution.
    x is the relative width,
    z is the absolute.
    """
    done_x = int(width * current_iter / total_iter)
    done_z = int(100 * current_iter / total_iter)
    message = message or 'Pulling'

    bar = ('█' * done_x) + ('-' * (width - done_x))
    print(f'\r{message}: |{bar}| {done_x}% ', end='')
    if current_iter == total_iter:
        _stdout_del_last_row()
