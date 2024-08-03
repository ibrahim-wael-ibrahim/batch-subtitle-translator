#!/bin/bash

# Clone the project repository
git clone https://github.com/ibrahim-wael-ibrahim/batch-subtitle-translator.git

# Navigate to the project directory
cd batch-subtitle-translator

# Install the package
pip install .

# Add alias to .bashrc (or .bash_profile or .zshrc)
echo 'alias translate="translate-subtitles $(pwd) $(pwd)"' >> ~/.bashrc

# Reload .bashrc to apply the changes
source ~/.bashrc

echo "Installation complete. You can now use the 'translate' command."
