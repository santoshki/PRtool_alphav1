import yaml
from yaml.loader import SafeLoader

with open('C:\\Users\\santosh.a.d.kulkarni\\PycharmProjects\\PRtool_alphav1\\database\\config.yaml') as confile:
    config_data = yaml.load(confile, Loader=SafeLoader)

db_details = config_data["database"]
db_hostname = db_details["db_hostname"]
db_name = db_details["db_name"]
db_username = db_details["db_username"]
db_password = db_details["db_password"]
secret_key = db_details["secret_key"]
