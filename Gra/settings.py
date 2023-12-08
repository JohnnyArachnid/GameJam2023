import json

# main game loop variable
main_loop_running = True

# converts python dictionary then saves it to config.json
def save_data(data):
    config_file = open("config.json", "w")
    
    json_object = json.dumps(data, indent=4)
    config_file.write(json_object)
    
    config_file.close()

# read config.json file then converts it to dictionary object
def load_data():
    config_file = open("config.json")
    
    data = json.load(config_file)
    
    config_file.close()
    
    # data is dictionary object, set of "key": "value"
    return data

config = load_data()