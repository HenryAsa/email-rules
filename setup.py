#!/usr/bin/env python3

"""
Setup for Gmail-Rules Package
"""

import os
from pathlib import Path
import sys
from setuptools import (setup, find_packages)


def setup_package():
    src_path = os.path.dirname(os.path.abspath(__file__))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    print(find_packages())

    metadata = dict(
        name="gmail_rules",
        author="Henry Asa",
        author_email="henryasa@mit.edu",
        description="Package to build Gmail Rules and Filters using Python",
        long_description=Path("README.md").read_text(encoding="utf-8"),
        long_description_content_type="text/markdown",
        url="https://www.henryasa.com",
        project_urls={
            "Bug Tracker": "https://github.com/HenryAsa/gmail-rules/issues",
        #     "Documentation": ,
            "Source Code": "https://github.com/HenryAsa/gmail-rules",
        },
        platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
        test_suite='pytest',
        python_requires='>=3.10',
        packages=find_packages()
    )
    # metadata['configuration'] = configuration
    print(metadata)
    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)
    return

if __name__ == '__main__':
    setup_package()
