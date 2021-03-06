# aciClient

A python wrapper to the Cisco ACI REST-API.

## Installation
``pip install aciclient``

## Installation for Developing
```
git clone https://github.com/netcloud/aciclient.git
pip install -r requirements.txt
python setup.py develop
```

## Usage

### Initialisation

### Username/password
```python
import aciClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

aciclient = aciClient.ACI(apic_hostname, apic_username, apic_password)
try:
    aciclient.login()
    
    aciclient.getJson(uri)
    aciclient.postJson(config)
    aciclient.deleteMo(dn)
    
    aciclient.logout()
except Exception as e:
    logger.exception("Stack Trace")
    
```

### Certificate/signature
```python
import aciClient
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

aciclient = aciClient.ACICert(apic_hostname, path_to_privatekey_file, certificate_dn)

try:
    aciclient.getJson(uri)
    aciclient.postJson(config)
    aciclient.deleteMo(dn)
except Exception as e:
    logger.exception("Stack Trace")
```

## Examples

### get config
```python
tenants = aciclient.getJson('class/fvTenant.json?order-by=fvTenant.dn|asc')

for mo in tenants:
    print(f'tenant DN: {mo["fvTenant"]["attributes"]["dn"]}')
```

### post config
```python
config = {
 "fvTenant": {
  "attributes": {
   "dn": "uni/tn-XYZ"
  }
 }
}

aciclient.postJson(config)
```

### delete MOs
```python
aciclient.deleteMo('uni/tn-XYZ')
```

## Testing

```
pip install -r requirements.txt
python -m pytest
```
## Contributing

Please read [CONTRIBUTING.md](https://github.com/netcloud/aciClient/blob/master/CONTRIBUTING.md) for details on our code 
of conduct, and the process for submitting pull requests to this project.

## Authors

* **Marcel Zehnder** - *Initial work*
* **Andreas Graber** - *Migration to open source*
* **Richard Strnad** - *Paginagtion for large requests, various small stuff*

## License

This project is licensed under MIT - see the [LICENSE.md](https://github.com/netcloud/aciClient/blob/master/LICENSE.md) file for details. 
