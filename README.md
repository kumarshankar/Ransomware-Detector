# Ransomware Detector
This is a Bidirectional LSTM based classifier that detects wannacry ransomware attack from time series data of hardware performance counters

## Overview
This project aims at detecting ransomware using LSTM

## Motivation
Ransomware attacks are one of the most prominent threats in cybersecurity. Preemptive detection of ransomware attack on computer systems and servers can help take corrective measures to prevent further damage. 

## Dataset 
Total number of features: 5
The dataset is of the form: instructions,cache-references,cache-misses,branches,branch-misses

The dataset is obtained from three sources.
regular sysntes    - measurement of normal system behavior.
ransomware affected systems - measurement of normal system behavior with ransomware working in the background.
special heavy compute systems - measurement of normal system behavior when a computational heavy program is running in the background which is not ransomware.




