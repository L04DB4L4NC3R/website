#!/bin/bash

set -euo pipefail

pip3 install requests
python3 get_posts.py
hugo
