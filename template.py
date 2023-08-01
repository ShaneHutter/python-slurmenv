#!/usr/bin/env python3
"""This is the base template for using python scripts as in SBATCH/SRUN via SLURM"""

from slurmenv import SlurmEnv

if __name__ == "__main__":
    for attr in SlurmEnv:
        print( f"{attr.name}\t{attr.value}")