import pytest
import unittest

class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True) #autouse param sets scope to all class methods
    def initdir(self, tmpdir):
        tmpdir.chdir() # change to pytest-provided temporary directory
        tmpdir.join("samplefile.ini").write("# testdata")

    def test_method(self):
        with open("samplefile.ini") as f:
            s = f.read()
        assert "testdata" in s
