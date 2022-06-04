#!/bin/bash

set -euo pipefail

pwd
ls 
python get_posts.py
hugo
