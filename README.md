
# Web Application Firewall (WAF) with Blockchain Logging

A Web Application Firewall (WAF) designed to filter and monitor HTTP requests, identifying and blocking common web attacks like SQL Injection and Cross-Site Scripting (XSS). The system logs all detected attacks into a tamper-proof blockchain, ensuring secure and verifiable attack records. This project utilizes a simple, interactive Streamlit interface for user inputs, making it easy to test and visualize potential vulnerabilities in web traffic.

# Features
SQL Injection Detection: Identifies and blocks common SQL Injection patterns.
XSS Protection: Detects and prevents Cross-Site Scripting (XSS) attacks.
Blockchain Logging: Logs attack attempts in a blockchain, ensuring tamper-proof attack records.
Streamlit Interface: User-friendly frontend for submitting text or files to check for vulnerabilities.
Real-Time Blockchain Display: View the blockchain of logged attacks directly from the Streamlit app.

# Tech Stack

Backend: Python
Regular expressions for detecting attacks.
Blockchain for secure logging.

Frontend: Streamlit
Interactive UI for inputs (text or file).

Real-time display of detected attacks and blockchain logs.
Blockchain: A simple Proof-of-Work blockchain for tamper-proof logging.

# Getting Started 

Prerequisites

Python 3.x installed

Install the dependencies using requirements.txt

pip install -r requirements.txt

Running the Application
Clone this repository:

git clone https://github.com/your-username/vulnerability_assessment_tool.github

cd vulnerability_assessment_tool

Run the Streamlit application:

streamlit run app.py

Open your browser and go to http://localhost:8501.

# Usage
Text Input: Enter text manually into the input box to check for vulnerabilities.

File Upload: Upload a .txt file to check for vulnerabilities.
The results will be displayed on the app, and any detected attacks will be logged into the blockchain.

You can view the blockchain of attacks directly on the Streamlit app.

# How It Works

WAF Logic:
The WAF uses regular expressions to detect common attack patterns like SQL Injection and XSS. It checks the text or file content against these patterns.

Blockchain Logging:
Any detected attack is recorded in a simple blockchain using a Proof-of-Work mechanism. Each block contains information about the attack and is cryptographically linked to the previous block, ensuring that logs are immutable and secure.

Streamlit Interface:
The Streamlit app provides a user-friendly interface where users can submit inputs for inspection and view the blockchain logs in real-time.

# Blockchain Details
Proof-of-Work: The blockchain employs a basic Proof-of-Work algorithm to validate new blocks.
Tamper-Proof: Each block contains a hash of the previous block, making the chain immutable and secure.

# Future Improvements
Add support for detecting other types of web attacks (e.g., CSRF).
Implement user authentication for logging into the system.
Create a more advanced blockchain consensus mechanism for distributed logging.

# Contributing

Fork the project
Create your feature branch (git checkout -b feature/YourFeature)
Commit your changes (git commit -m 'Add YourFeature')
Push to the branch (git push origin feature/YourFeature)
Open a pull request

# Acknowledgements
Streamlit documentation for interactive Python applications.
Blockchain tutorials for developing simple Proof-of-Work systems.
