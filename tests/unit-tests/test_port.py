import pytest
import sys
import os

sys.path.append(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '../..'))

from scans import Port


class TestPort():
    def test_null_validity(self):
        port = Port(None)
        assert port.valid() is False

    def test_string_validity(self):
        port = Port("22")
        assert port.valid() is False

    def test_21_validity(self):
        port = Port(21)
        assert port.valid() is False

    def test_22_validity(self):
        port = Port(22)
        assert port.valid() is True

    def test_23_validity(self):
        port = Port(23)
        assert port.valid() is False
