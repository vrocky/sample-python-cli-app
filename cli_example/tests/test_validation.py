
"""Module for testing the command-line argument validation."""
from unittest import mock

import pytest
import argparse


from cli_example.validation import validate_args

def test_validate_args():
    """Test the validate_args() function."""
    # Test with a valid input directory and file
    args = argparse.Namespace(input_dir='input_dir', file='input.txt')
    with mock.patch('os.path') as mock_os_path:
        mock_os_path.isdir.return_value = True
        mock_os_path.isfile.return_value = True
        validate_args(args)

    # Test with an invalid input directory
    args = argparse.Namespace(input_dir='invalid', file='input.txt')
    with mock.patch('os.path') as mock_os_path:
        mock_os_path.isdir.return_value = False
        with pytest.raises(ValueError):
            validate_args(args)


    # Test with an invalid input file
    args = argparse.Namespace(input_dir='input_dir', file='invalid.txt')
    with mock.patch('os.path') as mock_os_path:
        mock_os_path.isdir.return_value = True
        mock_os_path.isfile.return_value = False