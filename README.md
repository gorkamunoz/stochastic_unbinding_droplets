# Stochastic particle unbinding modulates growth dynamics and size of transcription factor condensates in living cells
## G. Muñoz-Gil et at. PNAS XXX (2022)

[![DOI](https://zenodo.org/badge/DOI/10.1101/2022.01.11.475940.svg)](https://doi.org/10.1101/2022.01.11.475940)

This repository contains the necessary tools to replicate most of the results from [our paper](). We offer three jupyter notebooks reviewing the main parts of the various numerical and machine learning tools used in the paper. 

Moreover, we freely distribute the experimental data used in the paper, namely, the trajectories of the Progesterone Receptor at various hormone concentrations. For details on this data, please check our paper and the associated supplementary material. We will be very happy to learn any new findings you may discover with this data! [Contact us](mailto:munoz.gil.gorka@gmail.com) for any news, comments or questions!

### Code

This repo contains three Jupyter notebooks, prepared for running with Python 3:

- `trajectory_analysis` : here we review the main characteristics of the used data, as well as calculating some classical information such as the diffusion coefficient and the turning angle distribution.
- `ml_analysis`: in this notebook we show how to train a neural network to characterize anomalous diffusion experimental data. Moreover, we show the various error metrics used in the paper to benchmark the method.
- `stochastic_unbinding_simulations`: last but not least, we show how to simulate the phenomenological model proposed in the paper.

**Requirements:** the previous notebooks need some libraries to run. You can install all of them via the requirements file using 

` pip install -r requirements.txt`

### Data

Aside of the previous notebooks, this repo also contains various data files, organized in three folders:

- **experimental_data**: this folder contains a single file, with various datasets of PR trajectories at different hormone concentrations can be found. The latter is a Matlab file. To open it with Python, check the beginning of the notebook  `trajectory_analysis.ipynb`.
- **ML_trained_models**: while we show how to train you own models in the notebok `ml_analysis`, you may not want to train you own model. In this folder you will find two pre-trained models, which you can load as shown in the aforementioned notebook.
- **figures**: contains some auxiliary figures used in this repo.



### Cite

We kindly ask you to cite our paper if any of the previous material was useful for your work:

```latex
@article{munoz2022particle,
title={Particle flow modulates growth dynamics and nanoscale-arrested growth of transcription factor condensates in living cells},
author={Mu{\~n}oz-Gil, Gorka and Romero-Aristizabal, Catalina and Mateos, Nicolas and Campelo, Felix and de LLobet-Cucalon, Lara Isabel and Beato, Miguel and Lewenstein, Maciej and Garcia-Parajo, Maria and Torreno-Pina, Juan Andres},
journal={bioRxiv},
year={2022},
publisher={Cold Spring Harbor Laboratory}
}
```



