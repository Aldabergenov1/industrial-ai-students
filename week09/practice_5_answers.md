# Practice 5: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. What is in the file (0.05 points)

**1.1** How many rows, exact duplicate rows and distinct mixes are there? How many mixes were tested at more than one age, and which ages occur?

Your answer:

...

**1.2** What range does the volume of the ingredients take, and why is it not exactly 1 m³?

Your answer:

...

**1.3** How many 28-day tests are there, and how many reach 40 MPa? Print the baseline with its ingredients, strength and energy, and plot strength against energy for the 28-day tests. What does the baseline do differently from a typical strong mix?

Your answer:

...

## Task 2. A surrogate for the strength, and a leak (0.08 points)

**2.1** Print the 3 × 2 table of cross-validated RMSE, with the difference between the two splits for each model.

Your answer:

...

**2.2** Which of the two splits is honest for *this* use of the model, and why? The optimiser will ask the model about mixes nobody has ever made.

Your answer:

...

**2.3** How big is the leak for each model? Which model would you pick as the surrogate, and what error in MPa should you expect from it on a new mix?

Your answer:

...

## Task 3. The objective and the constraints (0.04 points)

**3.1** Compute the energy, the volume and the predicted 28-day strength (MLP) of the baseline mix, and compare the predicted strength with the measured one. Print `penalised(base, mlp)`: is the baseline feasible for the surrogate?

Your answer:

...

**3.2** Take the baseline and cut the cement by 40 kg. Print energy, volume, predicted strength and the penalised value again. Which term of the penalty is active, and how big is it?

Your answer:

...

**3.3** The penalty weight is 1000 MJ per MPa. In one or two sentences: what would go wrong with a weight of 10?

Your answer:

...

## Task 4. Grid, random search and Nelder–Mead, written by you (0.08 points)

**4.1** Print a table: for each method the best mix found within the budget, its energy, predicted strength and volume, and the number of calls it used. Plot the best penalised value so far against the number of calls for the three methods, with the baseline energy as a horizontal line (Task 5 adds differential evolution to both).

Your answer:

...

**4.2** Which methods beat the baseline, by how many MJ and percent? Why does the grid do so badly with 2187 points?

Your answer:

...

**4.3** How many calls did the first Nelder–Mead run take, and did the restarts add anything?

Your answer:

...

## Task 5. Differential evolution, written by you, and a forest (0.08 points)

**5.1** Add DE to the table and the figure of Task 4. How does it compare with Nelder–Mead on the MLP?

Your answer:

...

**5.2** On the forest: how many calls does the *first* Nelder–Mead run take before it stops, and how far does it get from the baseline? What does DE find on the forest? Read the penalised value as well as the energy.

Your answer:

...

**5.3** Plot the predicted 28-day strength of both surrogates along one line: the baseline mix with the cement changed from 100 to 400 kg, everything else fixed. Explain from the plot why Nelder–Mead stalls on the forest and not on the MLP. Which kind of surrogate does a local optimiser need?

Your answer:

...

## Task 6. SQP, written by you: the constraints without a penalty (0.08 points)

**6.1** Report the SQP optimum on the MLP: the mix, its energy, strength and volume, the number of iterations and of calls to the model, and the stop message. Add SQP to the table of Task 5.

Your answer:

...

**6.2** Which constraints are active at the optimum? Read the multipliers: what is one MPa of the strength requirement worth, in MJ per m³? Compare it with the penalty weight $W = 1000$ of Task 3, and with the weight of 10 that Task 3 warned about.

Your answer:

...

**6.3** What happens to SQP on the **forest**, and why? Use the plot of Task 5.

Your answer:

...

## Task 7. How far can the optimum be trusted? (0.10 points)

**7.1** Take the best mix of Tasks 4–6, the lowest penalised value of the five methods, and check it three ways: what the forest predicts for it; the mean and standard deviation of the five networks; its distance to the nearest real mix against $D_{95}$. How many checks does it pass?

Your answer:

...

**7.2** Run the same checks on `best_ens`. What does the forest say now, and why is the agreement of five networks weak evidence?

Your answer:

...

**7.3** Run the checks on `best_both`. How much of the saving over the baseline is left, and which ingredients did the optimiser change?

Your answer:

...

**7.4** Print the nearest real mix to `best_both`: its ingredients and its *measured* strengths. Which of the optima would you dare to cast?

Your answer:

...

## Task 8. The safety margin and the recommendation (0.06 points)

**8.1** Print the table and plot both energies against the aim. Where does the optimiser save against the best real mix at the same aim, and where not?

Your answer:

...

**8.2** Your recommendation to the plant, in five to eight sentences: which mix goes to a **trial batch** first and with what aim; what the lab must measure; what you would do with the result (In-class work 9, Part 6.1, does the same with a dryer).

Your answer:

...

**8.3** Your conclusions in ten to fifteen lines: which optimiser you would use for this kind of problem and why, with the numbers of Tasks 4–6; what the surrogate's optimum of Tasks 4–6 is worth, and what the trusted one of Task 7 is worth; what single experiment would teach you the most about whether the saving is real.

Your answer:

...
