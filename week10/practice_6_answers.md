# Practice 6: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. A model from the step test (0.07 points)

**1.1** Plot the step test: valve and outlet temperature against time. Report $K$, $T$, $L$ of the two-point method on the smoothed curve and of least squares, with the RMS residual of each model.

Your answer:

...

**1.2** Plot the data with both fitted curves, with an inset on the first two minutes. Where does a first order plus dead time model miss this exchanger? Which of the two sets would you use, and why are the two dead times different?

Your answer:

...

## Task 2. Scoring a response, and the SIMC baseline (0.07 points)

**2.1** Report the SIMC gains and their overshoot, settling time and ITAE on the model.

Your answer:

...

**2.2** Run the same loop with $K_p$ twice as large. What happens to each of the three measures, and why?

Your answer:

...

**2.3** Which of the measures would you show to the plant manager, and which to an optimiser? Why?

Your answer:

...

## Task 3. The Ziegler–Nichols baseline (0.07 points)

**3.1** Report $K_u$, $P_u$ and the Ziegler–Nichols gains.

Your answer:

...

**3.2** Print a table of ZN and SIMC with the three gains and the three measures on the model, and plot both responses. Which is the better baseline for the optimisers to beat, and why must the comparison include both?

Your answer:

...

## Task 4. A genetic algorithm (0.12 points)

**4.1** Print `ga_table`, and the overshoot and settling time of `GA` on the model. How much lower is its ITAE than that of SIMC and of ZN?

Your answer:

...

**4.2** How far apart are the five results, in ITAE and in gains? Do different seeds find different tunings with the same ITAE, or the same tuning?

Your answer:

...

## Task 5. Particle swarm, and the equal budget (0.12 points)

**5.1** Print `pso_table`, and the overshoot and settling time of `PSO` on the model.

Your answer:

...

**5.2** One figure: the median and the range over the five seeds of the best-so-far ITAE against the number of evaluations, GA and PSO together (both use 30 evaluations per generation or iteration; a log scale on ITAE helps).

Your answer:

...

**5.3** Which method is better *on this budget*: in the median, in the worst seed, in speed? Do GA and PSO agree on the gains?

Your answer:

...

## Task 6. On the real exchanger (0.09 points)

**6.1** Print one table for the four tunings: the gains, and overshoot, settling time and ITAE on the model and on the exchanger. Plot the four responses of the exchanger.

Your answer:

...

**6.2** Did the ranking survive the move from the model to the plant? Which tunings got better and which got worse, and what in Task 1 could have warned you?

Your answer:

...

## Task 7. Robustness to the dead time (0.08 points)

**7.1** On the model, run the four tunings with the dead time $L$ times 1.25, 1.5 and 2. Print a table of overshoot and settling time. Which tunings stop settling?

Your answer:

...

**7.2** Print `robust_table`. Did every seed find the same tuning? What does that say about the robust cost?

Your answer:

...

**7.3** Compare `ROBUST` with `PSO` and with `SIMC` on the model at $L$, $1.5L$, $2L$, and on the exchanger with `extra_dead_time` 0 and 35 s. What does robustness cost on the nominal plant?

Your answer:

...

**7.4** Your recommendation and conclusions, in eight to twelve sentences: what GA and PSO gained over Ziegler–Nichols and over SIMC, in numbers, on the model and on the exchanger; what the choice between GA and PSO changed, compared with the choice of the cost function; which tuning goes into the controller, and what you would ask the plant engineers to measure first.

Your answer:

...

## Task 8 (optional). A physics-informed network finds the second lag (0.00 points)

**8 (optional).1** Train the PINN on the step test with seeds 0, 1, 2 and $\lambda$ = 1. For each seed print $K$, $T_1$, $T_2$, $L$ and the RMS misfit to the data.

Your answer:

...

**8 (optional).2** Check it by plain least squares: `curve_fit` of the exact step response of (1), $y = K\Delta u\,[1 - (T_1 e^{-s/T_1} - T_2 e^{-s/T_2})/(T_1 - T_2)]$ with $s = \max(0,\ t - t_s - L)$. Do the two agree?

Your answer:

...

**8 (optional).3** Train seed 0 once more with $\lambda$ = 10. What happens to the parameters, and why?

Your answer:

...

**8 (optional).4** One figure: the data, the PINN curve and the least-squares FOPDT of Task 1, with an inset on the first two minutes; next to it $T_1$, $T_2$, $L$ against the training step for $\lambda$ = 1 and 10. What do the two panels show?

Your answer:

...

**8 (optional).5** Retune on the new model. Write `simulate_loop2(Kp, Ki, Kd, K, T1, T2, L)`, the PID loop on (1) ($a_i = e^{-\Delta t/T_i}$, $x_1 \leftarrow a_1 x_1 + (1-a_1) K u$, $x_2 \leftarrow a_2 x_2 + (1-a_2) x_1$, the measurement is $x_2$; pass that step to `_pid_loop` with two states), and run `run_pso` (seed 0, the same 1500 evaluations) on its ITAE. Call the result `PSO2` and check it on the exchanger with `extra_dead_time` 0 and 35 s, next to PSO and ROBUST.

Your answer:

...

**8 (optional).6** Five to eight sentences. Where did the gain over Task 6 come from, the optimiser or the model? What did the PINN give here that `curve_fit` did not, and where would it give more? Did the better model fix the dead-time problem of Task 7?

Your answer:

...
