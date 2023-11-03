# Simple-Twitter-on-microservices

## Virtual environment

### Install

https://virtualenv.pypa.io/en/latest/installation.html 

```
# In some linux systems
sudo apt install python3-virtualenv
```

### Use

```
# Create environment with python3.10
virtualenv -p python3.10 env

# Access environmet
source ./env/bin/activate

# Exit environment
deactivate
```

## Install Requirements

    pip install -r requirements

```
# In some linux systems
sudo apt install uvicorn
```


## Run Services

```
cd src/services/<service-name>

uvicorn app.main:app --reload

# Run service in other port
uvicorn app.main:app --reload --port 8001

```
