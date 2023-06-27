from script import Addition
import os, sys

sys.path.insert(0, os.getcwd())


def test_add():
    subj = Addition(2, 3)
    assert isinstance(subj, int)
