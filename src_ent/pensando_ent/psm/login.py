import os
import logging
import sys
import json

def get_psm_config():
    HOME = os.environ["HOME"]
    psm_config_path = HOME+"/.psm/config.json"

    config_data = {}
    config_path = psm_config_path
    if not os.path.exists(psm_config_path):
        logging.warn("PSM config does not exist at "+ psm_config_path)
        cont = input("Create config at "+psm_config_path+" ? [y/n]")
        if cont.lower() != 'y':
            sys.exit(1)

        if psm_config_path[0] == "~":
            HOME = os.environ["HOME"]
            config_path = HOME + config_path[1:]
        foldersplit = config_path.split(os.sep)
        if foldersplit[-1]:
            dirpath = (os.sep).join(foldersplit[:-1])
            if not os.path.exists(dirpath):
                os.makedirs((os.sep).join(foldersplit[:-1]))
            config_data = update_psm_config(config_path)
        else:
            logging.error("Invalid PSM config path")
            sys.exit(1)
    else:
        with open(config_path, "r") as f:
            config_data = json.load(f)
    return config_data

def update_psm_config(path):
    psmip = input("Enter PSM IP address: ")
    try:
        with open(path, "w") as f:
            config_data = {"psm-ip": psmip}
            json.dump(config_data, f)
        return config_data
    except:
        logging.error("Unable to write to PSM config at:", path)
        sys.exit(1)

def write_psm_config(config_path, config_data):
    with open(config_path, "w") as f:
        psm_config = json.dump(config_data, f)
    return