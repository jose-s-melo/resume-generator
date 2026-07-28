import yaml

def load_data(file_path: str):
    
    if file_path.endswith(".yml") or file_path.endswith(".yaml"):
        with open(file_path) as file:
            return yaml.safe_load(file)
    
    