# Batch Subtitle Translator

A tool for translating subtitle files from English to Arabic.

## Features

- Automatically translates subtitle files (.srt) from English to Arabic.
- Uses Google Translator API.
- Supports batch processing of multiple subtitle files.
- Provides progress bars for translation status.

## Installation

You can install the Batch Subtitle Translator using a single command. This command will clone the repository, install the necessary dependencies, and set up the required alias.

### Prerequisites

- Ensure you have `git` and `pip` installed on your system.
- Ensure you have `python3` installed.

### Installation Command

Run the following command to install the package:

```sh
wget -nv -O- https://raw.githubusercontent.com/ibrahim-wael-ibrahim/batch-subtitle-translator/main/scripts/install.sh | bash

```

## Uninstall Command

To uninstall the `batch_subtitle_translator` package, follow these steps:

1. **Uninstall the Package**:

   Run the following command to uninstall the package:

   ```sh
   pip uninstall batch_subtitle_translator
   ```

2. **Verify Removal**:

   Check if the `translate-subtitles` command is still available:

   ```sh
   which translate-subtitles
   ```

   This should not return a path if the package was successfully uninstalled.

3. **Remove the Cloned Folder**:

   If you want to remove the folder where you cloned the project, navigate to the parent directory of the cloned folder and run:

   ```sh
   rm -rf ~/.batch-subtitle-translator
   ```
