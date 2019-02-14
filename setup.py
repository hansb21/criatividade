from setuptools import setup, find_packages

setup(
    name='calc',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calc = calc.__main__:run',
        ],
    },
)
