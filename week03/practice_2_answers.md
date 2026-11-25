# Practice 2: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. What is in the file (0.06 points)

**1.1** How many rows does each mode have, and how many hours does a file cover? Why did `d00.dat` need the special line in the loader?

Your answer:

...

**1.2** Which variables have far fewer distinct values than the others? Use `held` to say how long their values are held, and explain why.

Your answer:

...

**1.3** Report the range of `XMV10` in each mode. What is odd about fault 6, and from which hour of the file?

Your answer:

...

## Task 2. K-means and the elbow (0.10 points)

**2.1** Report the largest and the smallest raw standard deviation among the 52 variables. Why can standardisation not be skipped here?

Your answer:

...

**2.2** Plot `km_inertia` against $k$ and report the relative drop from $k-1$ to $k$. Is there an elbow?

Your answer:

...

**2.3** Crosstab the $k = 6$ clusters against `fault` and report `ari_k6`. Which faults did K-means find, which did it merge, and with what?

Your answer:

...

## Task 3. The silhouette (0.08 points)

**3.1** Plot `sil` against $k$ next to the ARI of each partition against `fault`. Which $k$ does the silhouette choose?

Your answer:

...

**3.2** Crosstab the best-silhouette partition against `fault`. What did it actually separate?

Your answer:

...

**3.3** The elbow, the silhouette and the true number of modes do not agree. Explain why a high silhouette can go with a partition that is useless to an engineer.

Your answer:

...

## Task 4. DBSCAN on the same data (0.10 points)

**4.1** Draw the k-distance plot with your $\varepsilon$ marked, and report a few quantiles of `kdist`. Why did you choose this $\varepsilon$?

Your answer:

...

**4.2** Report `eps_sweep`. What happens to the noise and the clusters as $\varepsilon$ grows?

Your answer:

...

**4.3** Crosstab `db_labels` against `fault`. Which modes end up as noise, which share a cluster?

Your answer:

...

**4.4** Why does one $\varepsilon$ not fit this data? Compare how spread out each mode is: the mean over the 52 columns of `Z[y == f].std(axis=0)`.

Your answer:

...

## Task 5. Comparing the two partitions (0.08 points)

**5.1** Crosstab K-means ($k = 6$) against your DBSCAN and report `ari_table`. Where do the two methods disagree most?

Your answer:

...

**5.2** Which modes do **both** methods separate, which does **neither**?

Your answer:

...

**5.3** For the modes neither method finds, use `shift`: which variables move, and by how much? Why does a fault visible in one variable hide in a 52-dimensional distance?

Your answer:

...

## Task 6. Which variables carry information (0.10 points)

**6.1** List the ten smallest raw variances and the ten smallest of `mm_var`. Is `XMEAS9`, the reactor temperature, a dead sensor? Use Task 1 and one sentence about what a controller does to the variable it controls.

Your answer:

...

**6.2** Report `n_high_corr` and the strongest pairs. Say what physical pair each of five of them is.

Your answer:

...

**6.3** Print the top ten of `mi_knn`, `mi_bin` and `mi_knn5` side by side, with $H(Y)$. The two estimators disagree about a whole group of variables. Which group, why is one estimator fooled, and how does `mi_knn5` confirm it?

Your answer:

...

## Task 7. A justified short list of five (0.15 points)

**7.1** Print the best three variables of `per_fault_mi` for each fault. Explain the best one of each fault physically.

Your answer:

...

**7.2** Write one line per variable of `FIVE`: what it is, which fault it covers, why you kept it over its neighbours. Report the largest $|r|$ inside the list.

Your answer:

...

**7.3** Report `ari_five` with the $k$ the silhouette chose and the crosstabs, and compare with `ari_k6` and the DBSCAN of Task 4. Which fault still hides inside normal operation after standard scaling?

Your answer:

...

**7.4** Why does it hide? Compare the standard deviation of your five over all data and within fault 0. What did `scale_to_normal` change, and if a fault is still merged, what are the other clusters spent on? Try one more $k$ or DBSCAN and report the ARI.

Your answer:

...

**7.5** Which five sensors would you keep on this plant, and what do you lose by keeping only them?

Your answer:

...
