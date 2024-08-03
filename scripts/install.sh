#!/bin/bash

# Define the hidden directory in the home directory
HIDDEN_DIR="$HOME/.batch-subtitle-translator"

# Clone the project repository into the hidden directory
git clone https://github.com/ibrahim-wael-ibrahim/batch-subtitle-translator.git $HIDDEN_DIR

# Navigate to the hidden directory
cd $HIDDEN_DIR

# Install the package
pip install .

# Define the alias command
ALIAS_CMD="alias translate='translate-subtitles $(pwd) $(pwd) '"

# Add the alias to the appropriate shell configuration file
if [ -f ~/.bashrc ]; then
    echo $ALIAS_CMD >> ~/.bashrc
    source ~/.bashrc
elif [ -f ~/.bash_profile ]; then
    echo $ALIAS_CMD >> ~/.bash_profile
    source ~/.bash_profile
elif [ -f ~/.zshrc ]; then
    echo $ALIAS_CMD >> ~/.zshrc
    source ~/.zshrc
else
    echo "No suitable shell configuration file found."
    exit 1
fi

# Make the Python script executable
chmod +x $HIDDEN_DIR/batch_subtitle_translator/translator.py

echo "Installation complete. You can now use the 'translate' command."
