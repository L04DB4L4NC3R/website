#!/bin/bash

set -euo pipefail

python get_posts.py
hugo
