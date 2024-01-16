# CURB 65 Calculator
A simple web app for calculating the CURB-65 score for pneumonia patients.

## Installation
From the command line, use command: `pip install shiny` to install the shiny package.

## Running
To run the app, navigate to the project directory in the command prompt, and use the command `shiny run src/launcher.py`

## Justifications
- Web Server Package - Shiny
  - Quick to get up and running.
  - Flexible for future extensions
  - One drawback is that it has not yet reached the first stable release, so some bugs are still being fixed
- Database Management - SQLite
  - Quick to get up and running
  - No external dependencies

## Other Questions for Researcher
- Are the units in the inputs correct for what you use?
- How many concurrent users will need to access this app?
- Will users need to access this from outside your local network?
- Are there any more features which would be useful to you if more time were avaliable?