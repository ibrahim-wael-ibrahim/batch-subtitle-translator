import os
import sys
from tqdm import tqdm
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator
import re

def extract_subtitle_blocks(content):
    return re.split(r'\n\n', content)

def translate_text(translator, text, src_lang, dest_lang):
    try:
        return translator.translate(text, source=src_lang, target=dest_lang)
    except Exception as e:
        print(f"Translation error: {str(e)}")
        raise

def translate_subtitle(input_file, output_file, src_lang='en', dest_lang='ar'):
    translator = GoogleTranslator(source=src_lang, target=dest_lang)

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    subtitle_blocks = extract_subtitle_blocks(content)
    translated_blocks = []

    filename = os.path.basename(input_file)
    custom_bar_format = f"{Fore.WHITE}{{l_bar:90}}{Fore.LIGHTGREEN_EX}{{bar}}{Fore.YELLOW}{{r_bar:50}}"
    progress_bar = tqdm(total=len(subtitle_blocks), desc=f"Translating {filename} blocks", bar_format=custom_bar_format)

    for block in subtitle_blocks:
        if block.strip():
            lines = block.split('\n')
            if len(lines) > 2:
                timestamp = lines[1]
                text_lines = lines[2:]
                text = ' '.join(text_lines)  # Combine text lines into a single string

                translated_text = translate_text(translator, text, src_lang, dest_lang)
                translated_block = f"{lines[0]}\n{timestamp}\n{translated_text}"
                translated_blocks.append(translated_block)

            progress_bar.update(1)

    progress_bar.close()
    translated_content = '\n\n'.join(translated_blocks)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_content)

def find_subtitle_files(input_dir, file_extension=".srt"):
    subtitle_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(file_extension):
                subtitle_files.append(os.path.join(root, file))
    return subtitle_files

def translate_file(input_file, input_dir, output_dir, src_lang, dest_lang):
    relative_path = os.path.relpath(input_file, input_dir)

    if not input_file.endswith("_en.srt"):
        input_file_with_suffix = input_file + "_en.srt"
        relative_path = os.path.relpath(input_file_with_suffix, input_dir)
    
    output_file = os.path.join(output_dir, relative_path.replace("_en.srt", "_ar.srt"))

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    if os.path.exists(output_file):
        return False

    translate_subtitle(input_file, output_file, src_lang, dest_lang)
    return True

def batch_translate_subtitles(input_dir, output_dir, src_lang='en', dest_lang='ar', max_workers=8):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files_to_translate = find_subtitle_files(input_dir, "en.srt")

    if not files_to_translate:
        print("No files to translate.")
        return

    custom_bar_format = f"{Fore.LIGHTMAGENTA_EX}{{l_bar}}{Fore.MAGENTA}{{bar}}{Fore.LIGHTRED_EX}{{r_bar:50}}"

    progress_bar = tqdm(total=len(files_to_translate), desc="Translating files", unit="file", bar_format=custom_bar_format)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(translate_file, file, input_dir, output_dir, src_lang, dest_lang) for file in files_to_translate]
        for future in as_completed(futures):
            if future.result():
                progress_bar.update(1)

    progress_bar.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: translate-subtitles <input_dir> <output_dir>")
        sys.exit(1)
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    batch_translate_subtitles(input_dir, output_dir)

if __name__ == "__main__":
    main()
