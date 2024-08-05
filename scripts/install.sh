#!/bin/bash

# Define the hidden directory in the home directory
HIDDEN_DIR="$HOME/.batch-subtitle-translator"

# Clone the project repository into the hidden directory
git clone https://github.com/ibrahim-wael-ibrahim/batch-subtitle-translator.git $HIDDEN_DIR

# Navigate to the hidden directory
cd $HIDDEN_DIR

# Make the Python script executable
chmod +x $HIDDEN_DIR/batch_subtitle_translator/translator.py
chmod +x scripts/translate.sh
chmod +x scripts/addEnInEnd.sh

# Install the package
pip install .


echo "Installation complete. You can now use the 'translate.sh' command."
