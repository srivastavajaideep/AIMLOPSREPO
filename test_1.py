import os
import sys
from script import Addition


sys.path.insert(0, os.getcwd())


def test_add():
    subj = Addition(2, 3)
    assert subj == 5
