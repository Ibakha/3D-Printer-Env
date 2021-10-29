# 3D-Printer-Env
Control &amp; monitor a 3D printer environment

## TODO: Change badges
![test](https://github.com/JudeBake/3D-Printer-Env/actions/workflows/test.yml/badge.svg)
[![coverage](https://codecov.io/gh/JudeBake/3D-Printer-Env/branch/develop/graph/badge.svg?token=WEAWM1E3HZ)](https://codecov.io/gh/JudeBake/3D-Printer-Env)

## Setup
### Install python
```
sudo apt update && sudo apt install -y python3 python3-pip python3-venv
```

### Clone the repo
```
git clone git@github.com:Ibakha/3D-Printer-Env.git
```

### Create the virtual environment
```
cd 3D-Printer-Env && python3 -m venv venv
```

### install dependencies
```
source venv/bin/activate && pip install -r requirements.txt
```

## Development
### Visual Studio Code
#### Usefull Extensions:
 - [cornflakes-linter](https://marketplace.visualstudio.com/items?itemName=kevinglasson.cornflakes-linter)
 - [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
 - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
 - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

#### Settings
In order for the linter to function properly, add the following to you ```.vscode/settings.json```
```
"python.pythonPath": "venv/bin/python3",
"python.analysis.extraPaths": ["./src"],
"cornflakes.linter.executablePath": "venv/bin/flake8"
```

### Run the tests
```
pytest
```

### Run tests + coverge
```
coverage -m pytest
coverage report
or
coverage htlm
```
