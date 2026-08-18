# Example workflow with Cedalion and snakemake

This repository demonstrates a simple group analysis (preprocessing and blockaveraing) of the motor dataset used in the [FRESH study](https://www.nature.com/articles/s42003-025-08412-1).

## Structure of the workflow

The structure of this repository follows [snakemake's guidelines for distribution and reproducibility](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html):

    .
    ├── config
    │   └── config.yaml
    ├── README.md
    ├── resources
    └── workflow
        ├── notebooks
        │   └── analyze_blockaverage.ipynb
        ├── scripts
        │   └── run_step.py
        └── Snakefile

The workflow is specifed in `workflow/Snakefile` and can be configured by editing `config/config.yaml`.


## Executing the workflow

To download the dataset and to execute the workflow run:

    snakemake -c 4 --report report.zip --report-after-run

Adapt the number of used cores (`-c 4`) to your machine. The workflow stores the downloaded dataset under `./resources`, creates processed files under `./results` and stores the rendered notebook under `./logs`. A report with data quality report figures is created and saved as `report.zip`. 