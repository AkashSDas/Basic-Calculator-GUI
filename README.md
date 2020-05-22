
# Basic Calculator GUI  

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/AkashSDas)

[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/AkashSDas)

[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE)

  
  

## Table of contents

  

*  [About](#about)

* [Technologies Used](#technologies-used)

*  [Installation](#installation)

*  [License](#license)

  
  

## About

> A simple `Calculator GUI` that can perform `addition`, `subtraction`, `multiplication` and `division`.

![Calculator](calculator.gif)

## Technologies Used

> [![](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) is used as Programming Language.

> Using Python module `Tkinter` to make `Calculator GUI`.

## Installation



#### With out using virtual-environment

`If you are just intersted in the GUI's script then follow the below instructions.`

- First, start by closing the repository
```bash
git clone https://github.com/AkashSDas/Basic-Calculator-GUI
```
- Go to the `src` folder
```bash
cd  Basic-Calculator-GUI/venv/src/
```

In folder `Basic-Calculator-GUI/venv/src/` there is `main.py` which is the GUI's script.

* To start the `GUI` do
```bash
python main.py
```


##### If you don't want to use virtual-environment then no need to proceed further since now you have the GUI script.

#### With using virtual-environment

>It is  **recommended** to use **`virtual enviroment`** for this project to avoid any issues related to dependencies.
 
Here **`pipenv`** is used for this project.

- First, start by closing the repository
```bash
git clone https://github.com/AkashSDas/Basic-Calculator-GUI
```

- Start by installing **`pipenv`** if you don't have it
```bash
pip install pipenv
```

- Once installed, access the venv folder inside the project folder

```bash
cd  'Basic-Calculator-GUI'/venv/
```

- Create the virtual environment

```bash
pipenv install
```

The **Pipfile** of the project must be for creating replicating project's virtual enviroment.

This will install all the dependencies and create a **Pipfile.lock** (this should not be altered).

 
- Enable the virtual environment

```bash
pipenv shell
```

* The `GUI` script is in `src` folder
```bash
cd src/
```
* To start the `GUI` do
```bash
python main.py
```


## License

  

This project is licensed under the MIT License - see the [MIT LICENSE](LICENSE) file for details.
