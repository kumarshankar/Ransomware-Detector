# Ransomware Detector
This is a Bidirectional LSTM based classifier that detects wannacry ransomware attack from hardware performance counters

## Overview
This project aims at detecting ransomware using LSTM

## Dataset 
Total number of features: 5
The dataset is of the form: instructions,cache-references,cache-misses,branches,branch-misses

There are three sources.
regular.txt    - measurement of normal system behavior.
ransomware.txt - measurement of normal system behavior with ransomware working in the background.
spec.txt       - measurement of normal system behavior when a computational heavy program is running in the background which is not ransomware.

