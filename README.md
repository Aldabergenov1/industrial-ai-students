# Industrial AI

Notebooks for the Industrial AI course at KBTU (Automation and Control). Every week has an
in-class work, done together in the class hour, and most weeks a graded practice that you finish
on your own. The data are real plant and test-rig records where possible, simulated where a real
record would not show the effect cleanly.

## Weeks

| week | topic | in-class work | practice | data |
|---|---|---|---|---|
| 0 | prerequisites: linear algebra, least squares, gradients, constrained optima, probability, with a self-check | [prerequisites](week00/prerequisites.ipynb) | | AI4I 2020, simulated |
| 1 | first look at industrial data: arrays, tables, signals, noise | [inclass_work_1](week01/inclass_work_1.ipynb) | | AI4I 2020 |
| 2 | from a raw plant export to an analysis-ready table: cleaning, outliers, PCA | [inclass_work_2](week02/inclass_work_2.ipynb) | [practice_1](week02/practice_1.ipynb) | AI4I 2020, pump sensors |
| 3 | clustering and informative features | [inclass_work_3](week03/inclass_work_3.ipynb) | [practice_2](week03/practice_2.ipynb) | hydraulic rig, Tennessee Eastman |
| 4 | knowledge representation, a model leaves the notebook | [inclass_work_4](week04/inclass_work_4.ipynb) | | AI4I 2020 |
| 5 | metrics, and a threshold from the cost of errors | [inclass_work_5](week05/inclass_work_5.ipynb) | [practice_3](week05/practice_3.ipynb) | AI4I 2020, SECOM |
| 7 | neural networks, Fourier, CNN, LSTM, attention, autoencoders, Q-learning | [inclass_work_7](week07/inclass_work_7.ipynb) | [practice_4](week07/practice_4.ipynb) | AI4I, pump sensors, CWRU bearings, a simulated room and fleet |
| 9 | optimising setpoints with an exact model and with a surrogate | [inclass_work_9](week09/inclass_work_9.ipynb) | [practice_5](week09/practice_5.ipynb) | simulated dryer, UCI Concrete |
| 10 | PID tuning by genetic algorithm and particle swarm | [inclass_work_10](week10/inclass_work_10.ipynb) | [practice_6](week10/practice_6.ipynb) | simulated furnace and heat exchanger |
| 11 | equipment diagnostics, FMEA, FTA, HAZOP, HAZID | [inclass_work_11](week11/inclass_work_11.ipynb) | [practice_7](week11/practice_7.ipynb) | hydraulic rig, NASA C-MAPSS |
| 13 | predicting a control object, artificial immune systems | [inclass_work_13](week13/inclass_work_13.ipynb) | [practice_8](week13/practice_8.ipynb) | simulated tank and motor, Tennessee Eastman |

There are no notebooks for week 6 (defences of practices 1–3), week 8 (midterm), week 12
(Quiz 2), week 14 (project defences) or week 15 (end-term).

## Running the notebooks

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Open a notebook from its week folder and run it top to bottom. The notebooks download their data
from Kaggle with `kagglehub` the first time they run; no account or token is needed. The few files
that are not on Kaggle are in `data/`, and the notebooks find them there. Keep the folder layout
of this repository, or at least keep `data/` in a folder above the notebook. See
[data/README.md](data/README.md) for the sources.

Notebooks that train networks (week 7 and the optional task of week 10) use an NVIDIA GPU when
PyTorch sees one and the CPU otherwise. For the GPU, install the CUDA build of PyTorch from
<https://pytorch.org/get-started/locally/> instead of the one in `requirements.txt`.

## Practices

Every task of a practice states a contract: the functions and result variables to write, with
their arguments, return values and units. How you write them is up to you, as long as you use the
method the task names. Under your cell a cell of public tests checks the code on small cases with
known answers; run it after your code.

You hand in two files:

1. the notebook, run top to bottom, named `Surname_Name_practice_N.ipynb`;
2. the answer sheet `practice_N_answers.md` from the same folder, filled in, named
   `Surname_Name_practice_N_answers.md`.

When you hand in, the notebook runs again from scratch, the public tests run together with hidden
ones that check the same contract on other inputs, and the share of passed tests gives the points
for the code. The answer sheet is marked by hand. A number in an answer that your notebook does not
print scores zero.

## License

Code under MIT (`LICENSE`), texts, notebooks and figures under CC BY 4.0
(`LICENSE-CONTENT.md`). The data sets keep the terms of their sources.
