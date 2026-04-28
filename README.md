# Problems and Prospects of Computational Fanfiction Research
## Github Repo for the AO3 practical session

Welcome to the repo for the AO3 practical session as part of the fanfiction workshop at DH Benelux 2026! 

This repo will contain the materials and guides we will need for the session. 
*Please read this readme carefully, as there will be a reading list and instructions for a pre-setup script you will need to run before the workshop*. 

## Repo structure
```
├── README.md
├── requirements.txt             <- dependencies for the session
├── setup.sh                     <- bash script to install and setup venv
├── test.py                      <- test script to run before the workshop
├── utils.py                     <- script with utility functions
├── developing_an_rq.ipynb       <- notebook for part 1
└── scraping_your_own_data.ipynb <- notebook for part 2
```

## Reading list
Before the workshop, I recommend reading the following paper. It will also be relevant throughout the day. 

[Jacobsen, M., & Kristensen-McLachlan, R. D. (2025). Beyond Style: Rethinking Computational Fanfiction Research. Journal of Data Mining & Digital Humanities.](https://jdmdh.episciences.org/16543/pdf) 

Additionally, it can be worth orienting yourself in the TOS and FAQ from AO3 as well as the following admin post.
[Section of TOS that contains info on data scraping](https://archiveofourown.org/tos#I.F)

[FAQ, contains info on use of tags and what is allowed on the archive](https://archiveofourown.org/tos_faq)

[AI and Data Scraping on the Archive — Archive of Our Own.](https://archiveofourown.org/admin_posts/25888)

## Setup and test scipts
To ensure the session runs as smooth as possible, I encourage you to do the following setup and test steps. 

1. install Chrome
We will be using a Chrome driver for the scraping part of the session. If you do not have Chrome installed already, please do so.

2. run setup.sh

The setup.sh script can be run from the terminal, e.g., in Visual Studio Code like so:
```
source setup.sh 
```
The script sets up a virtual environment and installs the necessary dependencies. 

3. run test.py

After running the setup script, you should make sure everything is setup correctly by running the test.py script:

```
python3 test.py
```

If the terminal prints "everything works as expected" then you are good to go.