#!/sur/bin/env python3

from distutils.core import setup

_pkg = {
    "name": "python-slurm-job",
    "version": "0.0.1",
    "author": "Shane Hutter",
    "author_email": "shane@intentropy.au",
    "description": "An importable Enum containing SLURM environment variables when launching a python application via sbatch and srun.",
    "licence": "MIT",
    "packages": [ "slurmenv" ],
    }

setup( **_pkg )