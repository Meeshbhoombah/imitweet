# -*- encoding: utf-8 -*-
"""
run.py

entry point for imitweet web app
"""

import os
import sys
from app import app

""" LAUNCH """
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = "0.0.0.0", port = port, use_reloader = True) # TODO - remove use_reloader?

