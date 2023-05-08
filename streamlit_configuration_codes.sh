#!/bin/bash

# Install required packages
apt-get update


# Install Python packages
pip install -r requirements.txt


# Create the Streamlit configuration file
mkdir -p ~/.streamlit/
echo "[server]"  > ~/.streamlit/config.toml 
echo "headless = true"  >> ~/.streamlit/config.toml
echo "port = $PORT"  >> ~/.streamlit/config.toml
echo "enableCORS = false"  >> ~/.streamlit/config.toml

# Run the application
python yourapplicationnameofheroku.py
