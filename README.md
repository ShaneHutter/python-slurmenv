# python-slurm-job

The goal of this package is to provide an importable Enum that contains
all data provided as environment variables.

You will need to ensure that this package is installed on all Nodes in the SLURM cluster and is available to the user leasing resources for a job in a resource partition.

The python script launched via srun when using sbatch should be able to reference environment variables like the following example:

This script should have each job append its node name and the CPUs on the node, to a file that is located in the same shared storage each node accesses the scripts from:
```
from slurmenv import SlurmEnv

if __name__ == '__main__':
    nodename = SlurmEnv.slurmd_nodename.value
    cpus_on_node = SlurmEnv.slurm_cpus_on_node.value
    output = f"Node: {nodename}\tCPUs: {cpus_on_node}"
    with open( "output" , "a" ) as output_file:
        output_file.write( output )
```