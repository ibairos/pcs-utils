### Setting up virtualenv

`python3 -m pip install virtualenv`
`virtualenv .`
`source bin/activate`
`pip install -r requirements.txt`
`sudo apt-get install xvfb`
`sudo apt-get install -y chromium-chromedriver`

### Execution

#### Running in Linux

`DRIVER=/path/to/chromedriver python test.py`

or, if the Chromedriver is in the PATH:

`python test.py`

#### Running in Mac

`MAC=true DRIVER=/path/to/chromedriver python test.py`