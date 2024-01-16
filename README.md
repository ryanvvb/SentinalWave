# SentinelWave 
*Advanced Radio Signal Classification for Network Security*

### Deep Learning Project
- CSCI 4931 Deep learning
- Fall 2023

### Collaborators
- Daniel Rodriguez
- Mahnoor Shahid
- Ryan Van Valkenburg

# Developer's Notes
### Problem statement: 
In the context of modern telecommunications and wireless communication systems, the security of radio signals is paramount. The increasing reliance on wireless technologies, coupled with the growing threats of interference, unauthorized access, and cyberattacks, necessitates the development of robust methods for classifying radio signals to ensure secure and reliable communication. 

### Motivation: 
Develop a security solution to identify potentially malicious radio signals and engage in defensive measures. FCC regulation effort to identify radio signals that are out of acceptable ranges from unlicensed users. 

### Method(s): 

	- Data: Radio signals (LTE and 2.4GHz band): Jupyter Notebook for Data collection 

	Collect radio signals using software defined radio devices 

	- Preprocessing: FFT, Mel scale, traditional scale normalization to convert audio signals into numerical 	data that can be processed and visual representations of the radio signals to be used in the CNN model. 

	- Model: ANN – Use deep learning techniques on a less powerful neural network to gauge performance 

        RNN – Attempt to use a recurrent model on a continuous radio signal data set 

        CNN – plan to scale and convert signals to visual data and classify with our CNN 

	Using a software defined radio to read radio waves/signals and determine/classify cellphone and Wi-Fi 	signals in the LTE and 2.4GHz range. We will be attempting multiple approaches to this using the models	specified above. 
 
### Timetable: 
	- September: Research and learn. Collect raw data/ clean data/ prep data 

	- October: First half – Train and test models. Adjust parameters based on performance metrics.  

        Second 	half – evaluate models and continue to make modifications to minimize error. 

    - November: before break- prep deliverables after break- prep presentation 

    - November 28th: Model presentation and demonstration.