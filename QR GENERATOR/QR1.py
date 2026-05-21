#!/usr/bin/env python3
"""
Launcher for the QR & Timer HTML page.

This project file was accidentally saved as a .py containing HTML. To fix that,
the HTML has been moved to `QR1.html`. Running this script will open the HTML
page in your default web browser.
"""
import webbrowser
from pathlib import Path


def main():
    html_path = Path(__file__).with_suffix('.html')
    if not html_path.exists():
        print(f"Missing HTML file: {html_path}\nIf you expected a Python app, please let me know.")
        return
    webbrowser.open_new_tab(html_path.as_uri())


if __name__ == '__main__':
    main()