# Stochastic particle unbinding modulates growth dynamics and size of transcription factor condensates in living cells
## G. Muñoz-Gil et at. PNAS XXX (2022)

Paper Doi: 
Repository Doi: 

This repository contains the necessary tools to replicate most of the results from [our paper](). We offer three jupyter notebooks reviewing the main parts of the various numerical and machine learning tools used in the paper. Moreover, we freely distribute the experimental data used in the paper, namely, the trajectories of the Progesterone Receptor at various hormone concentrations. For details on this data, please check our paper and the associated supplementary material. We will be very happy to learn any new findings you may discover with this data!

The repository is organized as follows. First, three jupyter notebooks, prepared for Python 3. If you want to run them in them online, you can find them in the Google Colab tool [here]().

- `trajectory_analysis` : here we review the main characteristics of the used data, as well as calculating some classical information such as the diffusion coefficient and the turning angle distribution.
- `ml_analysis`: in this notebook we show how to train a neural network to characterize anomalous diffusion experimental data. Moreover, we show the various error metrics used in the paper to benchmark the method.
- `stochastic_unbinding_simulations`: last but not least, we show how to simulate the phenomenological model proposed in the paper.

**Requirements:** the previous notebooks need some libraries to run. You can install all of them via the `requirements.txt` using 

` pip install -r requirements.txt`

As said, you can also run the codes in Google Colab [here]().