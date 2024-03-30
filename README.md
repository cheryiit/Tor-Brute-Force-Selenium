# Tor-Brute-Force-Selenium
Tor Brute-Force Selenium


Educational Tor Brute-Force Selenium Project
Overview
This project is an educational demonstration of a brute-force attack using Selenium automated with the Tor network for increased anonymity. It's designed to illustrate the potential vulnerabilities websites might have after a certain number of failed login attempts, typically leading to a reCAPTCHA challenge. This tool tries a list of passwords against multiple user accounts, showcasing how IP and user agent rotation can be leveraged to avoid detection and bypass security measures.

Features
Password Testing: Automates login attempts using a list of passwords from passwords.txt, testing up to 5 passwords per user account before encountering reCAPTCHA.
User Rotation: If a reCAPTCHA is detected or after trying the set number of passwords, it moves to the next user account in username.txt.
Tor Integration: Utilizes the Tor network to change the identys, all headers, IP and user agents (Actually Tor automaticly do this things) between attempts, 
aiming to evade security protections and mimic a more anonymous browsing environment.
Security Measures: Implements restarts of the network and Tor to refresh the connection settings, further avoiding detection.

Educational Purpose
This project is strictly for educational and testing purposes to demonstrate the technical feasibility of such attacks and encourage stronger security practices. It highlights the importance of implementing robust security measures on websites to protect against brute-force attacks. Users are solely responsible for the ethical use of this tool and any consequences arising from misuse.

Disclaimer
This tool is developed with the intention to promote cybersecurity education and should not be used for illegal activities. The author disclaims any liability for misuse or damage caused by this software.
