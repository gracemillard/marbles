# Marbles 

```this is a template I use for READMEs 
    I included a few templates I use a lot : requirements, setup, gitnore, vscode , logging
```


## Initialize Environment

```shell
conda create -n takehome python=3.8
conda activate takehome
cd src
pip install -r requirements-dev.txt -i https://pypi.org/simple
pip install -r handlers/requirements.txt -i https://pypi.org/simple
```

## About the code
-  you asked for "accessible and modular" so I included modifiable constraints (you can change the filters with the filters.json file in /resources)

## The Deployment Plan

My curent idea: <br />
- dockerize >> run on k8s >> maybe flask webservice to receive the json and some kinda load balencer 


## How to run test

```shell
cd src/handlers
python3 -m tests.test_marble
```

## Consideraions

-- How often will this be used ---> if infrequent will use lambda instead <br />
--- Where shall I store my modifiable config file? bucket or in memory?

## TO DOs
- NEED TO RUN MORE TESTS !!!!!!!  <br />
- write more details about deployment plan <br />
- figure out runtime complexity <br />


