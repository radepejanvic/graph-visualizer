# GRAPHV
## Graph visualization tool

Graphv is a plugin based  graph visualization tool used for displaying and exploring custom graph structured data. It contains various built-in plugins for easy beginning of data visualization. 
## Data source plugins

Designed to load specific structured data and parse it to graph model to make it possible for visualization.

- NBA data source 
- Crypto data source
- Flights data source
## Visualization plugins

Designed to display graph model using D3.js library.

- Simple visualizer
- Block visualizer

## Clone repo

HTTPS:
```console
https://github.com/radepejanvic/graph-visualizer.git
```
SSH: 
```console
git@github.com:radepejanvic/graph-visualizer.git
```
GitHub CLI:
```console
gh repo clone radepejanvic/graph-visualizer
```

## Create and activate virtual environment

Position yourself inside  `graph-visualizer` directory and run the following commands:
```console
py -m venv .env
.\.env\Scripts\activate
```

## Install plugins

```console
pip install -r requirements.txt
pip install -e .
```

## Run server

Position yourself inside `graph-explorer` directory and run the following commands: 
```console
py .\manage.py runserver 
```

## Run CLI app
```console
pip install .\core
graphv
```

Open browser and paste the following URL: 
```
http://127.0.0.1:8000
```

## Authors
- Nikola Trajković SV45/2021
- Rade Pejanović SV10/2021
- Veljko Ivanišević SV44/2021
- Marko Stojanović SV2/2021 - ???
