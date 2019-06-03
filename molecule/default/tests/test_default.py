# Some examples are given below.

import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    ("vim-enhanced"),
    ("screen"),
    ("tree"),
])
def test_common_pkg(host, name):
    pkg = host.package(name)

    assert pkg.is_installed
