# Automated Human-Readable Label Generation in Open Intent Discovery

## Instructions

### Setup
If running on a Sagemaker Studio notebook, choose the PyTorch 1.12 Python 3.8 GPU Optimized image on a GPU instance type then run the environment_setup.sh script.

### Run
The Jupyter notebook intent_label_generation.ipynb contains all the necessary steps to reproduce the experiments.

In the **Config** section, set the *mode* to either *'generate'* or *'evaluate'* and set the name of the *dataset* to either *'banking'*, *'clinc'* or *'snips'*.

Then, simply execute the remaining cells to either produce labels or evaluate already produced labels.

## Citation

If you use this source code in your work, please cite the paper:

    @inproceedings{anderson2024,
        author={Grant Anderson and Emma Hart and Dimitra Gkatzia and Ian Beaver},
        title={{Automated Human-Readable Label Generation in Open Intent Discovery}},
        year=2024,
        booktitle={Proc. INTERSPEECH 2024},
        pages={tbc},
        doi={tbc},
        issn={tbc}
    }
