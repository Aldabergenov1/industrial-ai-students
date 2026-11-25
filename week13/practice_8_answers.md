# Practice 8: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. The test stream and the unit cube (0.05 points)

**1.1** Which file is stored on its side, and how does the loader notice? How many hours does each file cover?

Your answer:

...

**1.2** Standardise every run with the mean and std of `X_train`. Plot the mean of $|z|$ over the 52 variables against the sample number for the runs of faults 1 and 9, with a vertical line at the onset. When does fault 1 become visible? Fault 9?

Your answer:

...

**1.3** Report `outside_share` and the worst variable. What does this say about 500 samples as a picture of "self", and why do we leave a margin around the box?

Your answer:

...

**1.4** The first 160 samples of each test run are normal too. Why do we not add them to the training data?

Your answer:

...

## Task 2. Negative selection in two variables (0.10 points)

**2.1** How many candidates were deleted? Plot the unit square: the self points, the detectors, and the samples of the runs of faults 1 and 4 after the onset.

Your answer:

...

**2.2** Report `pair_rates` and `normal_matched`. Which faults does this pair of variables see? Why is it blind to faults 2 and 7?

Your answer:

...

**2.3** Why are there false alarms on normal data, although 99 % of normal points lie within $r_s$ of self?

Your answer:

...

**2.4** Report `uncovered` and show the uncovered probes of the 300-candidate detectors on a second panel. Does negative selection guarantee that every abnormal state is covered?

Your answer:

...

## Task 3. The ROC curve and its area (0.07 points)

**3.1** Plot the ten ROC curves on one figure and print `AUC2`. Check two of your AUCs against `sklearn.metrics.roc_auc_score`.

Your answer:

...

**3.2** Mark on the curve of fault 1 the operating point of Task 2, $r_d = r_s$, and report its coordinates.

Your answer:

...

**3.3** Which faults have AUC near 0.5? What does an AUC of 0.5 mean for an operator, and what would an AUC well below 0.5 mean?

Your answer:

...

## Task 4. 52 variables, PCA and the curse of dimensionality (0.10 points)

**4.1** How much variance do the first 2, 3, 5 and 10 components explain? Report `k90`.

Your answer:

...

**4.2** Print `T4`. What happens with 52 variables? Use the numbers of the table: $r_s$, how many candidates were deleted, how far the candidates are from self.

Your answer:

...

**4.3** Which faults gain from the SPE column? What do these faults do to the plant, and why are they hard to see in the first three components?

Your answer:

...

## Task 5. V-detectors: a radius for every detector (0.08 points)

**5.1** How many V-detectors are kept on the common features, and what are the smallest, median and largest radius? Compare with $r_s$.

Your answer:

...

**5.2** Report `coverage_table`. Where does the constant radius cover more, where the V-detectors?

Your answer:

...

**5.3** Report `T5`. Why does a variable radius help more as the dimension grows? Which statement of the lecture about coverage do your numbers support?

Your answer:

...

## Task 6. From a score to an alarm: threshold and detection delay (0.10 points)

**6.1** Report `thr` and `T6`. Which faults are missed?

Your answer:

...

**6.2** Plot the score against the sample number for faults 1, 4 and 9 and for `X_normal`, with the threshold and the onset. Where do the top 1 % of `X_normal` come from?

Your answer:

...

**6.3** Compare the AUC of fault 4 with its delay. Why can a well-ranked fault alarm so late? Fault 15 gets an alarm after more than a day: is it detected?

Your answer:

...

**6.4** Try FAR = 1 % and 5 %, each with `confirm` = 1, 3 and 6. Print for each pair: the number of faults 1, 2, 4, 6, 7 caught and their mean delay, the delay of fault 4 and of fault 9, and the number of runs with a confirmed alarm **before** the onset. Is the early alarm of fault 9 at 5 % a detection? Which setting would you put into a control room?

Your answer:

...

## Task 7. Isolation Forest, One-Class SVM and the engineering comparison (0.15 points)

**7.1** Try `nu` = 0.01, 0.05, 0.2 for the SVM and `contamination` = "auto", 0.01, 0.1 for Isolation Forest on the common features. Which of them changes the AUC, which does not, and why?

Your answer:

...

**7.2** Print `auc_tab` and `delay_tab`, and per detector: the number of missed faults, the mean AUC over faults 1, 2, 4, 5, 6, 7, 11, and the false-alarm rate before the onset over all runs. Plot the ROC curves of the six detectors for fault 4.

Your answer:

...

**7.3** Constant radius and V-detectors have almost the same AUC. Why are their delays so different?

Your answer:

...

**7.4** Which faults are caught by every method, which by none? For faults 3, 9 and 15, is a better detector the answer, or is something missing in the data?

Your answer:

...

**7.5** **Conclusion**, 6–10 sentences for a plant engineer: which detector would you install, and on which features? What does negative selection give that the baselines do not, and what does it cost?

Your answer:

...
