#!/bin/bash
pip install poetry
source ~/.profile
cp -r ./my-c2l ~/my-c2l
cd ~/my-c2l
poetry install
poetry shell