
"""Module for parsing command-line arguments."""

import argparse

def parse_args():
    """Parse the command-line arguments.
    
    Returns:
        argparse.Namespace: The parsed arguments.
    """
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add a command-line argument
    parser.add_argument('input_dir', help='Input directory')

    # Add a command-line argument with a default value
    parser.add_argument('--file', default='input.txt', help='Input file')

    # Parse the command-line arguments
    return parser.parse_args()