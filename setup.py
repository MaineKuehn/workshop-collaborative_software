import os
from setuptools import setup, find_packages

repo_base_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(repo_base_dir, 'README.rst'), 'r') as README:
    long_description = README.read()

if __name__ == '__main__':
    setup(
        name="gksolite",
        version="0.9.0",
        description="gridka school game of life library",
        long_description=long_description.strip(),
        author="Eileen Kuehn, Max Fischer",
        author_email='maxfischer2781@gmail.com',
        url='https://github.com/MaineKuehn/workshop-collaborative_software',
        packages=find_packages(),
        # metadata for package search
        license='MIT',
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Education',
            'Topic :: Education',
            'Programming Language :: Python :: 3 :: Only',
        ],
        keywords='game-of-life gks',
        # unit tests
        test_suite='gksolite.gksolite_unittests',
    )
