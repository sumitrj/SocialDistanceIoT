## Social Distancing Violation Detection and Alert Actuation System

### Problem Motivation

The novel Coronavirus causes a lethal pulmonary disease COVID-19. The disease has affected more than 47.5 Million people worldwide. The contagion of the virus primarily spreadsthrough air but can travel within a radius of 2m. 

To avoid contracting the disease, it is mandatory to practice Social Distancing in public places. Despite being aware of this, people often tend to violate social distancing unconsciously. This is primarily seen in public places like retail shops,
public transport junctions, educational institutions and medical establishments.

### Proposed Solution
We aim to provide a solution to this problem by creating and implementing a system to 

a) Detect social distancing violation using Machine Learning algorithms based on live CCTV video feed and, 

b) Alert the people about the violation. 

### Solution architecture

To develop (a), we channel the CCTV live video-stream to a server(cloud) or raspberry pi(edge). Our software at the server/edge segments people, anchors locations, finds the distance between them and marks people who are not following social distancing. To develop (b), we divide the geographical area in the video frame into multiple parts. Each part has a buzzer/speaker/bulb which gets activated whenever a violation of social detection is detected in that part of the area. 

We have used an SVM based pedestrian detector for computationally un-intensive deployment.

### Merits
Our solution is unique and a better solution than the SOTA solutions in the way that

a) our system needs low processing power, hence doesn't need extra compute allocation and 

b) we have kept an automatic distributed alert system in the facility to reduce human intervention.


### For those who came looking for code
The file edge.py contains the python code that is to be run in the Raspberry Pi board with Relay modules connected to the designated GPIO pins.

