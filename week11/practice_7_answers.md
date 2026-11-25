# Practice 7: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. Run-to-failure data and the RUL label (0.07 points)

**1.1** How many engines are there, and how long do they live: minimum, median, maximum? Show a histogram of the lifetimes.

Your answer:

...

**1.2** Which of the 21 sensors and 3 settings carry no information? Say how you decided.

Your answer:

...

**1.3** Plot `s11` and `s4` against the true RUL for eight engines, RUL decreasing to the right. Where does the trend begin?

Your answer:

...

**1.4** Why do we train on $\min(\text{RUL}, 125)$? Back it with the correlation of `s11` with the RUL on rows where RUL > 125 and where RUL ≤ 125.

Your answer:

...

## Task 2. RMSE and the asymmetric score (0.07 points)

**2.1** Plot the score penalty of one engine against $d$ from −40 to +40, and $d^2$ scaled so that both agree at $d = -40$. Which side does the score punish more, and why would an airline want that?

Your answer:

...

**2.2** Take the true RUL of the validation points, `train.loc[idx_val, "RUL"]`. Report RMSE and score of three predictions: everyone 15 cycles early, everyone 15 cycles late, half early and half late.

Your answer:

...

**2.3** Take "everyone 15 cycles early" and make one engine 60 cycles late instead. What share of the total score comes from that one point, and what does it say about using this score alone?

Your answer:

...

## Task 3. Features from the past and a linear baseline (0.08 points)

**3.1** Report RMSE and score of the three baselines on the validation points.

Your answer:

...

**3.2** Check `"rolling"` against `sklearn.linear_model.Ridge(alpha=1.0)`: how far apart are the validation predictions?

Your answer:

...

**3.3** What do the slopes tell a linear model that one cycle cannot? Which change to `make_features` would leak the future, and what would the validation RMSE then tell you?

Your answer:

...

## Task 4. Gradient boosting with an asymmetric loss (0.10 points)

**4.1** For each ratio report the mean over the three seeds of RMSE, score and mean error $\bar d$, and the spread between seeds.

Your answer:

...

**4.2** Check the symmetric case: the RMSE of `ratio = 1` against `sklearn.ensemble.HistGradientBoostingRegressor` on the same data.

Your answer:

...

**4.3** Compare with your ridge from Task 3. What did the trees add?

Your answer:

...

**4.4** What does a larger ratio do to $\bar d$, to RMSE and to the score? Are the differences larger than the spread between seeds? Which ratio would you choose? (From Task 6 on, the common cell uses 1.5 for everybody.)

Your answer:

...

## Task 5. The test set, once (0.09 points)

**5.1** Report RMSE and score against `rul_test` for the three models, and the RMSE of boosting a second time against `np.minimum(rul_test, 125)`, which many papers use.

Your answer:

...

**5.2** Report the RMSE of boosting for true RUL in 0–25, 25–50, 50–100 and above 100, and plot predicted against true RUL. Which range is predicted best, and is that the range that matters?

Your answer:

...

**5.3** Print the five worst engines. What do they have in common?

Your answer:

...

## Task 6. From a prediction to an alarm: a one-sensor limit against the model (0.07 points)

**6.1** Print a table with the best sensor alarm and the model alarm: on time, late, missed, premature, the mean lead of the alarms on time and of all alarms. Which sensor is best?

Your answer:

...

**6.2** POD is the share of the 100 engines with an on-time alarm. Report both.

Your answer:

...

**6.3** The lead of an alarm is engine life you throw away. How many cycles per engine does each rule waste, as a share of the median lifetime? Why might a plant still prefer the rule with the larger waste?

Your answer:

...

## Task 7. FMEA: the risk priority number before and after (0.10 points)

**7.1** Fill the table: POD, its lower bound, D and RPN for HPC degradation before and after, and the RPN of the other four modes. Print the ranking before and after.

Your answer:

...

**7.2** What would D have been with the point estimate of POD instead of the lower bound? How many engines would you need to claim D = 1?

Your answer:

...

**7.3** Did the model reduce the risk of an HPC failure happening? What exactly has changed?

Your answer:

...

**7.4** FD001 contains only one failure mode. May you lower D of "Fan blade erosion" because the model watches the same sensors? What test would you ask for?

Your answer:

...

**7.5** Compare "Main bearing spalling" (S = 10) with "Fan blade erosion" (S = 6) in your table. Does the RPN order them the way a safety engineer would? What rule would you add?

Your answer:

...
