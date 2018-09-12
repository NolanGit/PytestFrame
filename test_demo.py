import os
import sys
import time
import pytest


def inc(x):
    return x + 1


def test_answer():
	time.sleep(5)
    assert inc(3) == 4
