"""Module for running the command-line interface."""

from cli import parse_args
from validation import validate_args

def main():
    """Run the command-line interface."""
    # Parse the command-line arguments
    args = parse_args()

    # Validate the arguments
    validate_args(args)

if __name__ == '__main__':
    main()
