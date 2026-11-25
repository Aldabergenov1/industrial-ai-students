# Practice 1: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. What is in the file (0.06 points)

**1.1** Report the shape of the table, the time span, the sampling step and the number of missing grid points. Is the clock regular?

Your answer:

...

**1.2** How many rows have each status, and when were the breakdowns? How much memory does the table take?

Your answer:

...

**1.3** Does `BROKEN` mark a period of failure or a single moment? What share of the rows are breakdowns, and what does that share mean for a model judged by accuracy?

Your answer:

...

## Task 2. Columns and rows that carry nothing (0.05 points)

**2.1** Which sensor is empty? How many rows repeat an earlier reading, as a count and as a share? Which five sensors have the longest constant run, in hours?

Your answer:

...

**2.2** Would you drop the repeated rows? Look at the timestamps of Task 1 before you answer.

Your answer:

...

**2.3** What does a constant run of several days say about a tag on a working pump, and what would you do with those sensors before modelling?

Your answer:

...

## Task 3. Gaps (0.10 points)

**3.1** Report the percentage missing for the worst ten sensors and the number of sensors under 0.1 %. Draw a missingness map (sensors against rows).

Your answer:

...

**3.2** Run `gap_lengths` on `sensor_50`, `sensor_51` and `sensor_00`: the number of gaps, the longest gap in hours, and the share of missing rows that sit in gaps longer than an hour. Are the gaps scattered samples or blocks?

Your answer:

...

**3.3** Split the sensors into three groups: drop the column, keep and flag, leave alone. Say where you put each boundary and why. Compare your choice with the common cell below.

Your answer:

...

**3.4** `sensor_50` misses about a third of its values. Would you trust a model that uses it? Back the answer with your numbers from question 2.

Your answer:

...

## Task 4. Outliers, and whether they are errors (0.10 points)

**4.1** Pick three sensors: the most symmetric one, the most skewed one, and `sensor_51`. For each, report the skew and the number of samples that 3-sigma, IQR and the robust z-score flag, and draw its histogram with both sets of fences on a log y-axis.

Your answer:

...

**4.2** What share of the whole file is `RECOVERING`? Report `iqr_recovering` for your three sensors and the five sensors with the highest share. What do the flagged samples have in common?

Your answer:

...

**4.3** Would you delete the flagged samples? Justify it with your numbers.

Your answer:

...

## Task 5. Resampling (0.09 points)

**5.1** Plot the hourly mean, max and std of `sensor_04` over the 48 hours around one of the breakdowns, with the breakdown marked. Quote the three aggregates for the day before the break and for the hour of the break.

Your answer:

...

**5.2** Which aggregate shows the failure coming, which hides it, and which only marks it? If none shows it coming, say so, and check a second breakdown before you conclude.

Your answer:

...

**5.3** What did going from minutes to hours cost? Name an event this table can no longer show.

Your answer:

...

## Task 6. Scaling (0.07 points)

**6.1** Box-plot the first ten sensors of `FEATS` raw, after min-max and after z-score. What does the raw panel hide?

Your answer:

...

**6.2** Report `broken_scaling`. What did one bad value out of all the rows do to each scaler?

Your answer:

...

**6.3** Which scaler would you take into Task 7, and why? Give two reasons.

Your answer:

...

## Task 7. PCA (0.10 points)

**7.1** How many components do you need for 90 % of the variance, and what share do the first two keep? Draw the scree plot with the cumulative curve on it.

Your answer:

...

**7.2** Project onto the first two components and plot all the minutes, coloured by `machine_status`, `NORMAL` first, small and faint. Report the mean position of each status on PC1 and PC2. Does the projection separate the pump's states?

Your answer:

...

**7.3** Name the five sensors that weigh most in PC1 and in PC2. How far apart are the first two eigenvalues, and what does that say about naming the components?

Your answer:

...

**7.4** In the in-class work two components of AI4I kept 75 %. Why does this data set need so many more?

Your answer:

...

## Task 8. The same PCA the other way round (0.08 points)

**8.1** Time both routes on `sub` and report the shape of the matrix each had to decompose.

Your answer:

...

**8.2** Print the first five shares of both routes, the largest difference between them, $\mu_i/\lambda_i$ for the first five, and whether the first two score columns agree. Explain each agreement from the SVD.

Your answer:

...

**8.3** How many eigenvalues of $\mathbf{G}$ are non-zero, and why that number? How much memory would $\mathbf{G}$ need for all the rows?

Your answer:

...

**8.4** Where do the two routes differ: what does each hand you, at what cost? When would you choose the Gram route?

Your answer:

...
