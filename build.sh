#!/bin/bash

set -euo pipefail

python3 get_posts.py
hugo
