#!/bin/bash
git pull
python version.py -p
python setup.py sdist upload -r https://:5550/pypi/
git add .
git commit -m "up api master стабильная"
git push