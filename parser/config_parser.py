import yaml
from yaml.loader import SafeLoader
from pathlib import Path

path = Path(__file__).parent / "../database/config.yaml"
with path.open() as file:
    data = yaml.load(file, Loader=SafeLoader)

db_value = data["database"]
db_location = db_value["db_location"]
db_name = db_value["db_name"]
db_secret_key = db_value["db_secret_key"]
db_hostname = db_location + db_name
password_reset_value = db_value["password_reset_value"]
