# bruteman
Configurable brute forcer for login forms

### Requirements

- Python 3.6

### Installation

```bash 
git clone https://github.com/xy3/bruteman.git 

cd bruteman

pip3 install .
```


### Usage


```bash

bruteman [-h] [-c CONFIG] [-o OUTPUT DIR] combos

```

### Making configs

Configs are written in [YAML](https://yaml.org/).

If the config argument is not set, you will be asked to choose a config from the config directory. You may make your own configs by following the format as layed out in `configs/example_config.yml`.

To gather the necessary headers and data for the config, go to the login page you wish to test and perform some requests while looking at the network tab in a browser debugger.