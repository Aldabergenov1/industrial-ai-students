# Practice 3: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. What is in the file (0.05 points)

**1.1** Which value of `Pass/Fail` means a failed lot, and how many lots of each are there? How accurate is a model that says every lot passes?

Your answer:

...

**1.2** Report the share of missing values, the number of signals more than half empty and the number of constant signals.

Your answer:

...

**1.3** Where does `Time` jump backwards? Quote two jumps with the dates before and after, say what went wrong, how you repaired it and what the true first and last dates are.

Your answer:

...

**1.4** Plot or print the failed lots per week. Are failures spread evenly over the three months?

Your answer:

...

## Task 2. The confusion matrix (0.07 points)

**2.1** At the threshold 0.5, give the confusion matrix and the accuracy of each model on the test part, and the accuracy of "every lot passes".

Your answer:

...

**2.2** What did each model do with the failed lots? Look at the largest score the forest gives to any test lot and explain where it comes from.

Your answer:

...

## Task 3. Precision, recall, F1 and the threshold (0.07 points)

**3.1** Precision, recall and F1 of both models on the test part at the threshold 0.5.

Your answer:

...

**3.2** Plot precision, recall and F1 against the threshold on the out-of-fold scores, both models. Which threshold gives the best F1 for each, and what are precision and recall there?

Your answer:

...

**3.3** Why is choosing the threshold on out-of-fold development scores allowed, and choosing it on the test scores not?

Your answer:

...

## Task 4. The ROC curve and its area (0.10 points)

**4.1** ROC-AUC of both models on the test part, by your `auc_by_pairs` and by `roc_auc_score`. Plot both ROC curves with the diagonal of a coin.

Your answer:

...

**4.2** The fab can afford to inspect 5 % of the good lots for nothing. What share of the failed lots does each model catch at a false-alarm rate of 5 %? And at 10 %?

Your answer:

...

**4.3** Explain the forest's ROC-AUC in words, with the pairs definition: what exactly is that probability?

Your answer:

...

## Task 5. The precision-recall curve (0.10 points)

**5.1** AP of both models on the test part, with your function and with `average_precision_score`. What AP does a coin get here, and how many times better than the coin is each model? Plot both PR curves with the coin's level.

Your answer:

...

**5.2** The dilution ×10: which metric moved, which did not, and why?

Your answer:

...

**5.3** You report to the fab manager, who will read the number as "how good are the alarms". Which of the two metrics do you put in the report, and what do you write next to it?

Your answer:

...

## Task 6. The threshold from the cost of an error (0.13 points)

**6.1** Plot the cost against the threshold on the out-of-fold development scores, both models, with the two fixed policies. Which threshold is cheapest for each, and at what cost?

Your answer:

...

**6.2** Open the test part, once. One table: the cost of "inspect nothing", "inspect every lot", each model at 0.5, at $t^* = 1/21$ and at its development threshold, with a column "cost per 100 lots".

Your answer:

...

**6.3** Which policy do you recommend to the fab? Choose it by the development costs, the same way you chose the thresholds; the test table only says what that choice costs. How much does it save on the test part against the best policy that needs no model?

Your answer:

...

**6.4** Should $t^*$ work for these models? Are their scores calibrated probabilities (look at how the common cell trains them)? If a model looks cheap at $t^*$ on the test part anyway, would you trust that?

Your answer:

...

## Task 7. The same models, in time order (0.12 points)

**7.1** Is the order of the rows the order of the repaired time? Give the dates and the failed lots of the past and of the future.

Your answer:

...

**7.2** ROC-AUC and AP on the future, next to the random-split numbers of Tasks 4–5, and the failure rate of each test part.

Your answer:

...

**7.3** What does the forest policy of Task 6 cost on the future, against "inspect every lot" and "inspect nothing"?

Your answer:

...

**7.4** Which of the two sets of numbers would you put in a report to the fab, and why? What could have changed between August and October?

Your answer:

...

**7.5** Your conclusion in three or four sentences: the metric you would use to compare models on SECOM, the threshold you would install with what it costs per 100 lots, and how far you trust that number after this task.

Your answer:

...
