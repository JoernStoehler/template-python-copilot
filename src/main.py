"""Main module for the project.

This module demonstrates a basic structure for Python projects with proper typing,
docstrings, and function organization.
"""

import logging
from pathlib import Path

import yaml
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()


def load_config(config_path: str | Path) -> dict:
    """Load configuration from a YAML file.

    Args:
        config_path: Path to the configuration YAML file

    Returns:
        Dictionary containing the configuration

    Raises:
        FileNotFoundError: If the config file doesn't exist
        yaml.YAMLError: If the YAML file is malformed
    """
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path) as file:
        try:
            config = yaml.safe_load(file)
            logger.info(f"Configuration loaded from {config_path}")
            return config
        except yaml.YAMLError as e:
            logger.error(f"Error parsing configuration file: {e}")
            raise


def process_data(data: list[float], scale: float = 1.0) -> list[float]:
    """Process a list of numeric data.

    This is a simple example function that scales a list of numbers.

    Args:
        data: List of numeric values to process
        scale: Scaling factor to apply to each value

    Returns:
        List of processed values
    """
    logger.debug(f"Processing data with scale factor: {scale}")
    return [value * scale for value in data]


def main(config_path: str | None = None) -> None:
    """Main entry point for the application.

    Args:
        config_path: Optional path to configuration file
    """
    logger.info("Starting application")

    # Example usage of functions
    if config_path:
        config = load_config(config_path)
        logger.info(f"Loaded configuration: {config}")

    # Example data processing
    sample_data = [1.0, 2.5, 3.7, 4.2]
    processed = process_data(sample_data, scale=2.0)
    logger.info(f"Processed data: {processed}")

    logger.info("Application finished")


if __name__ == "__main__":
    main()
