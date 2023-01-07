from unittest import mock

"""Module for testing the command-line argument parsing."""


import pytest
import argparse
from cli_example.cli import parse_args



def test_parse_args():
    """Test the parse_args() function."""
    # Test with no arguments
    #with pytest.raises(SystemExit):
    #   parse_args()

    # Test with valid arguments
    with mock.patch('sys.argv', ['input_dir',"c:\\", '--file', 'input.txt']):
        args = parse_args()
        assert args.input_dir == 'c:\\'
        assert args.file == 'input.txt'