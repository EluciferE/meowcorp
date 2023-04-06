from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
    "python-dotenv~=0.21.0",
    "sqlalchemy~=1.4.39",
    "psycopg2~=2.9.5",
    "aiogram~=2.23.1"
]

setup(
    name="meowcorp",
    version="0.1.3",
    packages=find_packages(include=['meowcorp', 'meowcorp.*', 'meowcorp.conf.project_template.*']),
    description="Add-on to the library of aiogram",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/EluciferE/meowcorp/",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'meowcorp-admin = meowcorp.commands:execute_from_command_line',
        ]
    }
)
