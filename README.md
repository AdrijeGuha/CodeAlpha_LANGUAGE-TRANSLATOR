# Language Translator Python Program

![Language Translator]([translator_screenshot.png](https://github.com/AdrijeGuha/CodeAlpha_LANGUAGE-TRANSLATOR/blob/c5105867e4fffbc9f08a8949d77273eb6278b788/img/translator_screenshot.png))

## Overview

This Python project aims to provide a user-friendly Graphical User Interface (GUI) for translating text content from one language to another in real-time. The program utilizes the `customtkiter` library for GUI development and the `googletrans` library for language translation.

## Features

- Real-time language translation with a single button click.
- User-friendly interface for input and output text.
- Supports translation between a wide range of languages.

## Prerequisites

Before running the program, ensure you have the following libraries installed:

- [customtkiter](https://github.com/TomSchimansky/CustomTkinter)
- [googletrans](https://github.com/ssut/py-googletrans)

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

The requirements.txt file is present in this repo itself.

## How to Use

1. Clone this repository to your local machine.
2. Install the required libraries as mentioned in the "Prerequisites" section.
3. Run the `translator.py` script to launch the GUI application.

## Getting Started

1. Import the necessary modules from `customtkiter` and `googletrans`.
2. Create a GUI window with input and output text areas and a "Translate" button.
3. Implement the translation function using the `googletrans` library.
4. Link the "Translate" button to call the translation function and update the output text area accordingly.

## Limitations

- The program requires an active internet connection to access the Google Translate service.
- Due to the limitations of the Google Translate API, extensive usage may be rate-limited.
- The GUI library has set limitations, demining the applications' user-friendly aspect.

## Contributions

Contributions to improving the project, adding new features, fixing bugs, or enhancing the GUI are welcome. Just create a pull request, and we'll review it together.

## License

This project is licensed under the MIT License. See the [LICENSE]([LICENSE](https://github.com/AdrijeGuha/CodeAlpha_LANGUAGE-TRANSLATOR/blob/42316f1fe05c0ddda2e7a0becb4ff901ef593524/LICENSE)https://github.com/AdrijeGuha/CodeAlpha_LANGUAGE-TRANSLATOR/blob/42316f1fe05c0ddda2e7a0becb4ff901ef593524/LICENSE) file for details.
