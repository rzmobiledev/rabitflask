#!/bin/bash

set -e

python manager.py db init --directory models/migrations
python manager.py db migrate
python main.py