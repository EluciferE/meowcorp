from setuptools import setup, find_packages

requirements = [
    "python-dotenv~=0.21.0",
    "sqlalchemy~=1.4.39",
    "psycopg2~=2.9.5",
    "aiogram~=2.23.1"
]

setup(
    name="meowcorp",
    version="0.1",
    packages=find_packages(include=['meowcorp', 'meowcorp.*', 'meowcorp.conf.project_template.*']),
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
