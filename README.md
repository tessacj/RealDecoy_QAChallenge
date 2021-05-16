# RealDecoy_QAChallenge
Submission by Tessa John


Project Description

The chosen language for this project was Python with use of Selenium, Python's Unittest, and Allure for report generation. The project was done in a virtual environment (pipenv) and was tested on Chrome Browser with an M1 Macbook Air (Arm Architecture). 

Pre-requisites for Set-up
Python 3.9
pip3
pipenv


Set-Up Instructions

1. Download this git repository to your machine and unzip it to a suitable directory.
2. Install the `chromedriver` plugin, unzip it, and add it to your device's path. In the case of MacOS, move it to the /usr/local/bin path. In the case of Windows you would need to add the path of the driver to your environment variables. *Chrome drivers can be found at https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/, the appropriate driver should be installed corresponding to your browser's version*
    NB *It would've been more suitable to set up a remote driver for selenium which would eliminate step 2 but due to timing, I had to forego this option.
3. Open the project directory in your device's terminal
4. Run the command `pipenv install` to install the dependencies of this project which can be found in the Pipfile. (This command would work for MacOS and Linux. In the case of Windows, install the requirements from the requirements.txt file using the command `pip3 install -r requirements.txt`)

This should be all that is required for setup.


Running the Project

1. While the project directory is open in terminal, activate the virtual environment of your project with the command `pipenv shell`
2. Run the project with the command `python3 -m pytest testcases/test_saucedemo.py --verbose --alluredir ./new_test_report` (--alluredir creates a directory to hold the test report.)
3. After the project has run, you can view the report with the command `allure serve ./new_test_report`

As there is a compiled test report already in this repository, you can use the command `allure serve ./saucedemo_test_report` to view the report. 

Please reach out if there are any questions. 
