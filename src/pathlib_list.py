#!/bin/env python
import sys
from pathlib import Path

if sys.argv[1] == "r":
    a = list(Path("data").glob("**/*"))
else:
    a = list(Path("data").glob("**"))
