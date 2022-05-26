# AMD Pensando PSM Python Bindings
This repo contains the python language bindings for the REST APIs exposed by AMD Pensando Policy and Services Manager (PSM). Client bindings differ and thus reflect the functions in various PSM distributions:
* [Cloud Distribution](src_cloud/pensando_cloud/README.md)
* [Enterprise Distribution](src_ent/pensando_ent/README.md)
* [Distributed Services Switch Distribution](src_dss/pensando_dss/README.md)

## Getting started

1. Requirements

```
Python >= 3.6
```

2. Use pip to install the desired distribution

```sh
pip install pensando-cloud
```

3. import the cloud APIs and start fetching the objects

```
import os
from pensando_cloud.psm.apis import ClusterV1Api
from pensando_cloud.psm import configuration, api_client

import warnings
warnings.simplefilter("ignore")

configuration = configuration.Configuration(
    psm_config_path = os.environ['HOME'] + "/.psm/config.json",
    interactive_mode = True
)
configuration.verify_ssl = False

client = api_client.ApiClient(configuration)
api_instance = ClusterV1Api(client)
response = api_instance.get_cluster()
[...]
```

More apps [here](https://github.com/pensando/psm-tools/tree/main/client/python/examples) using python apis.

## Learn more about PSM API
* Concepts: [API structure](docs/PSMAPI.md) or in PSM installation at `https://<PSM IP Address>/docs`
* PSM API specification: Swagger schema at `https://<PSM IP Address>/generated/swaggeruri.html`
* PSM GUI `Admin` menu, allows `Enable Live Capture` to see the the APIs used when an operation is performed in PSM GUI

## Contributing
The AMD Pensando Python SDK is auto generated from the PSM swagger spec. Please do not fork/modify any code in this repository, instead head over to [https://github.com/pensando/psm-tools](https://github.com/pensando/psm-tools) to generate the appropriate code.

## Issues
Please submit an issue at [https://github.com/pensando/psm-tools/issues](https://github.com/pensando/psm-tools/issues) if you find a bug or want to request an enhancement.
