"""Module for validating command-line arguments."""

import os

def validate_args(args):
    """Validate the command-line arguments.
    
    Args:
        args (argparse.Namespace): The parsed arguments.
    
    Raises:
        ValueError: If the input directory or file is invalid.
    """
    # Validate the input directory
    if not os.path.isdir(args.input_dir):
        raise ValueError(f'Invalid input directory: {args.input_dir}')

    # Validate the input file
    if not os.path.isfile(args.file):
        raise ValueError(f'Invalid input file: {args.file}')