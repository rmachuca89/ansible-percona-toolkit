"""Test for the ansible percona-toolkit role."""
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_percona_toolkite_package(host):
    """Test corresponding package is installed."""
    pt_pkg = host.package("percona-toolkit")

    assert pt_pkg.is_installed
