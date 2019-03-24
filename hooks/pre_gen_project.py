#!/usr/bin/env python
import os
import sys

PROJECT_DIR = os.path.realpath(os.path.curdir)
PARENT_DIR = os.path.dirname(PROJECT_DIR)

if os.path.exists(os.path.join(PARENT_DIR, 'docker-compose.yaml')):
    print('Error: docker-compose.yaml already exists.')
    sys.exit(1)
