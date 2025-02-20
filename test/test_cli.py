"""Test the CLI"""

import os
import filecmp
import pdb

import pytest

@pytest.fixture(scope='session', autouse=True)
def clear_out_directory():
    """Delete all files in test/out"""
    folder = os.path.dirname(os.path.realpath(__file__)) + '/out'
    for filename in os.listdir(folder):
        if not filename == '.gitignore':
            file_path = os.path.join(folder, filename)
            os.unlink(file_path)
    yield

def test_cli():
    exit_status = os.system('python -m manyworlds --help')
    assert exit_status == 0

def test_cli_hierarchy_output():
    os.system('python -m manyworlds --input test/fixtures/scenarios_forest.feature --output test/out/scenarios_flat_strict_cli.feature > test/out/scenarios_hierarchy.txt')
    assert filecmp.cmp('test/out/scenarios_hierarchy.txt',
                       'test/fixtures/scenarios_hierarchy.txt')
