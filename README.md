# HBV UK Setup


[![release](https://img.shields.io/github/v/release/openclim/hbv-setup)](https://github.com/OpenCLIM/hbv-setup/releases/latest)
[![build](https://github.com/OpenCLIM/hbv-setup/actions/workflows/build.yml/badge.svg)](https://github.com/OpenCLIM/hbv-setup/actions/workflows/build.yml)

This DAFNI model extracts a zip file containing HBV input data.

## Usage 
```
docker build -t hbv-setup .
docker run -v "<absolute_path_of_data_directory>:/data" --name hbv-setup hbv-setup
```
or
```
python setup_funcs.py
```
## Documentation
[hbv-setup.md](docs/hbv-setup.md)

To build the documentation:
```
cd docs
python build_docs.py
```