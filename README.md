Introduction
============
The test project for RMR to calculate scalar product of 2 vectors.

Problem description:

There is 2 compressed vectors. Program should calculate scalar product of
these vectors.

Compression means that each odd item in a list is a value and each even item is
a count of value in decompressed vector.

How To Setup Test Requirements
==============================
To install the requirements we need to create virtual environment and setup all required pip packages:

```
  virtualenv -p python3 .env
  source .env/bin/activate
  pip install -r test-requirements.txt
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
