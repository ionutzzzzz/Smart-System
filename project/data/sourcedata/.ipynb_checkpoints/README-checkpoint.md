# Overview

This is a MI-BCI dataset from the 2019 World Robot Conference Contest-BCI Robot Contest MI

In brief, it contains two-class motor imagery data from 53 participants and three-class motor imagery data from 11 participants.

> Two-class tasks: left hand-grasping, right hand-grasping, three-class tasks: left hand-grasping, right hand-grasping and foot-hooking.
> Raw data and Preprocessed data.

# Citing this dataset

Please cite as follows:

> 

# License
The `Brain Computer Interface Motor Imagery-EEG Dataset` dataset is made available under the ODC-BY.

Copyright (c), Banghua Yang, Fenqi Rong

See the `LICENSE` file.
A human readable information can be found at:

https://creativecommons.org/licenses/by/4.0/

# Format

The dataset is formatted according to the Brain Imaging Data Structure (BIDS).
See the `dataset_description.json` file for the specific version used.

Generally, you can find metadata in the `.tsv` files and documentation thereof in the accompanying `.json` files.
For example `participants.tsv` contains metadata about the participants,
and `participants.json` contains documentation about the columns in `participants.tsv`

An important BIDS definition to consider is the 'Inheritance Principle',
which is described in the BIDS specification under the following link:

https://bids-specification.readthedocs.io/en/latest/common-principles.html#the-inheritance-principle

In brief, the Inheritance Pinciple states that any metadata file (such as `.json`, `.tsv`)
may be defined at any directory level, but no more than one applicable file may be defined at a given level [...],
and the values from the top level are inherited by all lower levels -- unless they are overridden by a file at the lower level.

# Details about the experiment

For a detailed description of the task, see Banghua Yang et al. (2024)
and the supplied `task-motorimagery_eeg.json` file.
