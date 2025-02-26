from setuptools import setup, find_packages

setup(
    name="batch_subtitle_translator",
    version="0.2",  # Updated version
    packages=find_packages(),
    install_requires=[
        "tqdm",
        "colorama",
        "deep_translator",
    ],
    entry_points={
        'console_scripts': [
            'translate-subtitles=batch_subtitle_translator.translator:main',
        ],
    },
    scripts=['scripts/translate.sh', 'scripts/addEnInEnd.sh'],
    author="Ibrahim Wael Ibrahim",
    author_email="ibrahim.wael.ibrahim@outlook.com",
    description="A tool for translating subtitles str files from en to ar",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/ibrahim-wael-ibrahim/batch-subtitle-translator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
