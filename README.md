# CS50AI Exercises Solution

## Overview
This repository contains all of my code for the solution of the CS50AI exercises.

This project requires a specific Python environment to run, which can be easily set up using Conda. Below are the instructions to create and activate the Conda environment using the provided `environment.yml` file.

## Prerequisites
Make sure you have [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your system.

### Installing Conda
If you don't have Conda installed, you can install it by downloading [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution).

---

## Setting Up the Environment

### Step 1: Clone the Repository
First, clone the project repository to your local machine.

```bash
git clone https://github.com/do-ald533/cs50AI.git
cd your-project
```
---

### Step 2: Create the Conda Environment
Create the Conda environment from the environment.yml file by running the following command:

```bash
conda env create -f environment.yml
```

This will install all the required dependencies and create a new Conda environment.

---

### Step 3: Activate the Environment
Once the environment is created, you need to activate it:

```bash
conda activate cs50ai
```

---

### Step 4: Verify Installation
To ensure everything is set up correctly, you can list the installed packages with:

```bash
conda list
```