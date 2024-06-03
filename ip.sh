#!/bin/bash
echo "==IP-RECON SETUP=="

# Update package lists for both Termux and Linux
if [ "$(uname)" == "Linux" ]; then
  sudo apt update
else
  pkg update
fi

# Install Python packages using the appropriate package manager
if [ "$(uname)" == "Linux" ]; then
  sudo apt install git python python2 python3
else
  pkg install git python python2 python
fi

# Install pip3 for Python 3 (if not already installed)
if ! command -v pip3 &> /dev/null; then
  sudo apt install python3-pip  # For Linux
  pkg install python3-pip        # For Termux
fi

# Install Python libraries using pip3
pip3 install pyfiglet colorama requests
