"""Tests for the main module."""

import os
import tempfile
from pathlib import Path

import pytest
import yaml

from src.main import load_config, process_data


def test_process_data():
    """Test the process_data function with different inputs."""
    # Test with default scale factor
    data = [1.0, 2.0, 3.0]
    result = process_data(data)
    assert result == [1.0, 2.0, 3.0]

    # Test with custom scale factor
    result = process_data(data, scale=2.5)
    assert result == [2.5, 5.0, 7.5]

    # Test with empty list
    assert process_data([]) == []


def test_load_config():
    """Test the load_config function."""
    # Create a temporary config file
    config_data = {
        "name": "test-project",
        "version": "0.1.0",
        "settings": {"debug": True, "log_level": "INFO"},
    }

    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as temp_file:
        temp_path = Path(temp_file.name)
        yaml.dump(config_data, temp_file)

    try:
        # Test loading the config
        loaded_config = load_config(temp_path)
        assert loaded_config["name"] == "test-project"
        assert loaded_config["version"] == "0.1.0"
        assert loaded_config["settings"]["debug"] is True
        assert loaded_config["settings"]["log_level"] == "INFO"
    finally:
        # Clean up temporary file
        os.unlink(temp_path)


def test_load_config_file_not_found():
    """Test load_config raises FileNotFoundError for missing files."""
    with pytest.raises(FileNotFoundError):
        load_config("nonexistent_config.yaml")


def test_load_config_invalid_yaml():
    """Test load_config raises YAMLError for invalid files."""
    # Create a temporary file with invalid YAML
    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as temp_file:
        temp_path = Path(temp_file.name)
        temp_file.write(b"name: test\n  invalid indentation")

    try:
        # Test loading the invalid config
        with pytest.raises(yaml.YAMLError):
            load_config(temp_path)
    finally:
        # Clean up temporary file
        os.unlink(temp_path)
