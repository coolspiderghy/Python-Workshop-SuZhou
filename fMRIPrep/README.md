# Neuroimaging in Python: fMRIPrep
> Xiangzhen Kong, Zhejiang Univeristy
> https://person.zju.edu.cn/konglab#lab

### Installation
Two ways
- [Mannually prepared enviroment](https://fmriprep.org/en/stable/installation.html#manually-prepared-environment-python-3-7) (Python 3.7+)
- Use container technologies (RECOMMENDED), e.g., [Docker](https://fmriprep.org/en/stable/docker.html#run-docker) and [Singularity](https://fmriprep.org/en/stable/singularity.html#run-singularity)

### Usage Notes
fMRIPrep can be ran via the command *fmriprep* directly, or via the command *docker run*, or via the *fmriprep-docker* wrapper. The *fmriprep-docker* accepts all of the typical options for fMRIPrep. To simplify the practice, we use *fmriprep-docker* for this course.  
- [Command-Line Arguments](https://fmriprep.org/en/stable/usage.html)

### Examples
`docker run -rm hello-world`

`python -m pip install --user --upgrade fmriprep-docker`

`fmriprep-docker .\ds003030\ .\output\ participant --fs-licence-file .\license.txt`

`fmriprep-docker .\ds003030\ .\output\ participant --fs-licence-file .\license.txt --fs-no-reconall`

File *license.txt* is the FreeSurfer license file, which can be applied via this [link](https://surfer.nmr.mgh.harvard.edu/registration.html). When you receive the license file, put a copy to the main folder (i.e., the same folder as *output*, *ds003030_select*, and *README.md*). 

**To be updated ...**

### Links
fMRIPrep https://fmriprep.org/en/stable/index.html

Nipype https://nipype.readthedocs.io/en/latest/
