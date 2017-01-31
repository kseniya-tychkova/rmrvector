Introduction
============
The test project for RMR to calculate scalar product of 2 vectors.

How To Setup Requirements
=========================
To install the requirements we need to create virtual environment and setup all required pip packages:

```
  virtualenv -p python3 .env
  source .env/bin/activate
  pip install -r requirements.txt
```

How To Run
==========
To execute the code you should run the command:

```
  python rmrvector/rmrvector.py --input rmrvector/input.txt
```

How To Run Unit Tests
=====================
To execute the unit tests you should run the command:

```
  py.test
```
