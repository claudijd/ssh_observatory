import pytest
import sys
import os

sys.path.append(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '../..'))

from scans import Target


class TestTarget():
    def test_loopback_validity(self):
        target = Target("127.0.0.1")
        assert target.valid() is False

    def test_magic_url_validity(self):
        target = Target("169.254.169.254")
        assert target.valid() is False

    def test_private_addresses(self):
        target = Target("192.167.1.1")
        assert target.valid() is True
        target = Target("192.168.1.1")
        assert target.valid() is False
        target = Target("192.169.1.1")
        assert target.valid() is True
        target = Target("10.0.0.0.1")
        assert target.valid() is False
        target = Target("172.16.0.0.1")
        assert target.valid() is False

    def test_resolves_validity(self):
        target = Target("ssh.mozilla.com")
        assert target.valid() is True
        target = Target("notarealdomainname.mozilla.com")
        assert target.valid() is False
        target = Target("ssh.mozilla.com")
        assert target.valid() is True
        target = Target("github.com")
        assert target.valid() is True
