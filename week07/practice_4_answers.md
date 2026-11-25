# Practice 4: answer sheet

Name: ...

Answer under each question in a few sentences, with the numbers your notebook printed. A number that the notebook does not print scores zero.

## Task 1. What is in the files (0.05 points)

**1.1** How long is each recording, and which one is shorter than the rest? How many windows of 2048 samples does that leave it?

Your answer:

...

**1.2** What is the shaft speed, and how long is one window in milliseconds and in shaft revolutions?

Your answer:

...

**1.3** Which file holds two recordings, under which variables, and which of them is the record named in the file? What is the other one, by the catalogue? Which one did the feature table use (give the three maxima), and what would a model trained on that table have learned about "IR014"?

Your answer:

...

**1.4** Plot 0.1 s of the drive-end signal of `normal`, `IR021`, `B021` and `OR021`, one panel each, the same vertical scale. Describe what you see.

Your answer:

...

## Task 2. The baseline from Practice 3 (0.05 points)

**2.1** On the validation part, give the accuracy and macro-F1 of both models and the F1 of every state.

Your answer:

...

**2.2** Plot the validation confusion matrix of the better model with the state names on the axes. Which states are recognised perfectly, and which are confused with which? Is the confusion between fault *locations* (ball against inner race) or between *sizes* of the same fault?

Your answer:

...

**2.3** Why macro-F1 and not only accuracy here, although the classes are almost the same size?

Your answer:

...

## Task 3. The network (0.04 points)

**3.1** How many weights does the network have? Count them by hand from the layer sizes and check with `sum(p.numel() for p in net.parameters())`. How does that compare with the number of training windows?

Your answer:

...

**3.2** Print the three numbers of `hist` at epochs 0, 10, 50, 100, 200 and 299.

Your answer:

...

**3.3** Where is the validation loss lowest, and what is the validation accuracy there and at epoch 299?

Your answer:

...

## Task 4. Learning curves (0.05 points)

**4.1** Plot the learning curves of `[64, 64]`: train and validation loss on one axis, validation accuracy on a second panel, the epoch of the lowest validation loss marked. Describe the three stages you see, with epochs. What happens to the gap between the two losses?

Your answer:

...

**4.2** The validation loss at epoch 299 is much worse than at its minimum, yet the validation accuracy hardly moved. How can both be true? (Think about what cross-entropy punishes that accuracy does not see.)

Your answer:

...

**4.3** Plot the validation losses of the three sizes. Which one underfits, which one overfits fastest? Give the lowest validation loss of each and its epoch.

Your answer:

...

## Task 5. Early stopping (0.04 points)

**5.1** Report the epoch it stopped at, the best epoch, and the validation loss and accuracy of the restored network. Compare with Task 3: the best epoch there, and the network at epoch 299. Plot the curves of this run with both epochs marked.

Your answer:

...

**5.2** Why must the saved weights be a *copy*? What would `self.best_state = net.state_dict()` give you after training, and which public test catches it?

Your answer:

...

**5.3** Early stopping chooses the epoch on the validation part. Is the validation accuracy of the restored network an honest estimate for new data? Why does Task 6 use the test part?

Your answer:

...

## Task 6. The network against the baseline, on the test part (0.10 points)

**6.1** One table on the test part: accuracy and macro-F1 of the logistic regression, the forest and the early-stopped network.

Your answer:

...

**6.2** Give the mean, the smallest and the largest test macro-F1 over the five seeds of each model, and the training time of each.

Your answer:

...

**6.3** Plot the test confusion matrix of the seed-0 network. Which states does it confuse? Are they the same as for the forest in Task 2?

Your answer:

...

**6.4** Is the network better than the forest? Answer with the spread over seeds, not with one pair of numbers. Then say which model you would install on a motor, and why. Training time, the number of weights and what a maintenance engineer can check are fair arguments.

Your answer:

...

**6.5** Ball faults are the hard ones. One possible physical reason: a ball spins and rolls, so its defect does not touch the races at every pass. Look at your Task 1 figure for B021: does it look more like `normal` or like `IR021`?

Your answer:

...

## Task 7. The spectrum and the defect frequencies (0.04 points)

**7.1** Plot the amplitude spectra of the first second of `normal`, `IR021`, `OR021` and `B021` up to 6 kHz, logarithmic vertical axis. Where does the energy of the faulty bearings sit compared with the healthy one?

Your answer:

...

**7.2** Plot their envelope spectra from 0 to 500 Hz with the shaft speed and the three defect frequencies marked. Give the strongest envelope line of each state. Which of them sits on its own defect frequency? Which does not, and what does that tell you about the ball fault?

Your answer:

...

## Task 8. The spectrogram (0.06 points)

**8.1** Plot the spectrograms of the first 0.1 s of `normal`, `IR021` and `OR021`, power in decibels (`10 * np.log10(S + 1e-12)`), one colour scale for all three, up to 24 kHz. In which frequency band do the strikes show up?

Your answer:

...

**8.2** How many strikes in 0.1 s and what median gap do you measure for OR021 and IR021? Compare with one period of the BPFO and of the BPFI.

Your answer:

...

**8.3** In IR021 the stripes are not all equally strong. Why would an inner race defect be struck harder at some moments? (Which part of the bearing turns with the shaft?)

Your answer:

...

## Task 9. Spectral features and the network of Section 1 (0.07 points)

**9.1** Test macro-F1 of the forest and of the network on the band energies, and the F1 of every state for the network.

Your answer:

...

**9.2** Compare with Section 1, where 16 time-domain features from **two** sensors gave a test macro-F1 of about 0.92 with the ball faults as the weak states. What happened to the ball faults, and why do the bands carry more?

Your answer:

...

**9.3** A result this good on CWRU should make you suspicious. Each state is one recording. What could the band energies have learned besides the fault? (Think about everything that differs between two recordings made on different days.)

Your answer:

...

## Task 10. A CNN on the raw signal (0.07 points)

**10.1** Print the best epoch, the training time, and the test macro-F1 and per-state F1 of the CNN.

Your answer:

...

**10.2** Put three results side by side: the Section 1 network on 16 time features, the Task 9 network on 32 band energies, this CNN on the raw signal. Count the weights of the CNN and of the Task 9 network. Which needed somebody to design the features, and which found its own?

Your answer:

...

**10.3** Plot two or three of the 16 first-layer filters (`cnn[0].weight`). Do they look like anything? (A short burst at a few kHz would be a strike detector.)

Your answer:

...

## Task 11. An autoencoder that knows only the healthy bearing, and a fault at another load (0.08 points)

**11.1** Give the threshold, and the share of test windows above it for `normal` and for each fault.

Your answer:

...

**11.2** **The 3 hp recording.** `raw_217` is IR021 at another motor load; no model has seen it. What do the forest and the network of Task 9, the CNN of Task 10 (count the predicted states) and the autoencoder (share above the threshold) say about it? Which models recognise IR021, which see a fault at all, and which call it normal?

Your answer:

...

**11.3** One paragraph for a maintenance engineer: which of the two tools, "which fault" or "something is wrong", would you trust on a motor running at a load it was never trained on, and why? What can you not check with these data?

Your answer:

...
