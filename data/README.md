# Data

The notebooks find a data set with `dataset_folder(name)`, defined in their first cell. It
downloads a Kaggle data set with `kagglehub` (cached after the first time) and falls back to
`data/<name>/` when Kaggle is out of reach. For work without internet, run each notebook once
while online: the cache then serves it offline.

## On Kaggle, downloaded by the notebooks

| name | Kaggle | what it is | weeks |
|---|---|---|---|
| `ai4i` | [stephanmatzka/predictive-maintenance-dataset-ai4i-2020](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020) | AI4I 2020 predictive maintenance, S. Matzka; UCI id 601 | 1, 2, 4, 5, 7 |
| `pump_sensor` | [nphantawee/pump-sensor-data](https://www.kaggle.com/datasets/nphantawee/pump-sensor-data) | water pump sensor log | 2, 7 |
| `hydraulic` | [jjacostupa/condition-monitoring-of-hydraulic-systems](https://www.kaggle.com/datasets/jjacostupa/condition-monitoring-of-hydraulic-systems) | hydraulic test rig, ZeMA gGmbH; UCI id 447 | 3 |
| `tep` | [red2yang/tennessee-eastman-profbraatz](https://www.kaggle.com/datasets/red2yang/tennessee-eastman-profbraatz) | Tennessee Eastman process, R. Braatz's files | 3, 13 |
| `secom` | [paresh2047/uci-semcom](https://www.kaggle.com/datasets/paresh2047/uci-semcom) | SECOM semiconductor manufacturing; UCI id 179 | 5 |
| `cwru` | [brjapon/cwru-bearing-datasets](https://www.kaggle.com/datasets/brjapon/cwru-bearing-datasets) | Case Western Reserve University bearing data | 7 |
| `concrete` | [maajdl/yeh-concret-data](https://www.kaggle.com/datasets/maajdl/yeh-concret-data) | concrete compressive strength, I-C. Yeh; UCI id 165 | 9 |
| `cmapss` | [behrad3d/nasa-cmaps](https://www.kaggle.com/datasets/behrad3d/nasa-cmaps) | NASA C-MAPSS turbofan degradation | 11 |

The terms of use are on each Kaggle page and at the original source.

## In this folder

| name | file | what it is | weeks |
|---|---|---|---|
| `hydraulic_cycles` | `hydraulic_cycles/hydraulic_cycles.csv` | mean and std of the hydraulic rig sensors per cycle | 11 |
| `work_orders` | `work_orders/work_orders.csv` | simulated maintenance work orders | 11 |
| `exchanger` | `exchanger/exchanger_step_test.csv` | simulated step test of a heat exchanger | 10 |

Some quirks of the data are left on purpose, because finding them is part of a task. Do not
"fix" the files: the SECOM `Time` column and the two records in CWRU `IR014_1_175.mat`.
