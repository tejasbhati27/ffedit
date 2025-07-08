# Entry point for ffedit CLI/Gradio interface

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import cv2
import numpy as np
from ffedit.core import cli

if __name__ == "__main__":
    cli()
