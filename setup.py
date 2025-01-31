from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="icloudpd",
    version="1.8.0",
    url="https://github.com/icloud-photos-downloader/icloud_photos_downloader",
    description=(
        "icloudpd is a command-line tool to download photos and videos from iCloud."
    ),
    maintainer="The iCloud Authors",
    maintainer_email=" ",
    license="MIT",
    packages=find_packages(),
    install_requires=required,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"console_scripts": ["icloudpd = icloudpd.base:main"]},
)
