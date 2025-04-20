#!/usr/bin/env python
"""Example utility script.

This script demonstrates how to structure a utility script in this project.
It includes proper logging, argument parsing, configuration, and error handling.
"""

import argparse
import logging
import sys
from pathlib import Path

from dotenv import load_dotenv

# Add the parent directory to path so we can import from src
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.main import load_config, process_data

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Example utility script for data processing"
    )
    parser.add_argument("--config", type=str, help="Path to configuration file")
    parser.add_argument(
        "--data", type=str, required=True, help="Path to input data file"
    )
    parser.add_argument(
        "--output", type=str, help="Path for output file (default: output.txt)"
    )
    parser.add_argument(
        "--scale", type=float, default=1.0, help="Scaling factor for data processing"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    return parser.parse_args()


def read_data(file_path: str) -> list[float]:
    """Read numeric data from a file.

    Args:
        file_path: Path to the input file

    Returns:
        List of numeric values read from the file

    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file contains invalid numeric data
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    try:
        with open(path) as f:
            return [float(line.strip()) for line in f if line.strip()]
    except ValueError as e:
        logger.error(f"Invalid data in file: {e}")
        raise


def save_results(results: list[float], output_path: str) -> None:
    """Save results to a file.

    Args:
        results: List of results to save
        output_path: Path to save results to
    """
    with open(output_path, "w") as f:
        for value in results:
            f.write(f"{value}\n")
    logger.info(f"Results saved to {output_path}")


def main() -> int:
    """Main function for the script.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    # Load environment variables
    load_dotenv()

    # Parse command line arguments
    args = parse_args()

    # Configure logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load configuration if provided
        config = load_config(args.config) if args.config else {}
        _ = config

        # Read input data
        logger.info(f"Reading data from {args.data}")
        data = read_data(args.data)
        logger.info(f"Read {len(data)} values")

        # Process data
        scale_factor = args.scale
        logger.info(f"Processing data with scale factor: {scale_factor}")
        results = process_data(data, scale=scale_factor)

        # Save results
        output_path = args.output or "output.txt"
        save_results(results, output_path)

        return 0
    except Exception as e:
        logger.error(f"Error running script: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
