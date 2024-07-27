import json

class JSONHelper:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_data(self, data):
        """Save data to a JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def load_data(self):
        """Load data from a JSON file."""
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_value(self, key):
        """Get a specific value from the JSON file using a key."""
        data = self.load_data()
        return data.get(key)

    def update_variable(self, variable_name, key):
        """Update a specific variable with the value from the JSON file."""
        value = self.get_value(key)
        globals()[variable_name] = value

    def update_variables(self, variable_map):
        """Update multiple variables with values from the JSON file.

        Args:
            variable_map (dict): A dictionary mapping variable names to JSON keys.
        """
        data = self.load_data()
        for variable_name, key in variable_map.items():
            globals()[variable_name] = data.get(key)

"""
# Example usage
if __name__ == "__main__":
    # Initialize the JSONHelper with the path to the JSON file
    json_helper = JSONHelper('data.json')

    # Save initial data to the JSON file
    initial_data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    json_helper.save_data(initial_data)

    # Update a specific variable
    json_helper.update_variable('name', 'name')
    print(name)  # Output: Alice

    # Update multiple variables
    variable_map = {'name': 'name', 'age': 'age', 'city': 'city'}
    json_helper.update_variables(variable_map)
    print(name)  # Output: Alice
    print(age)   # Output: 25
    print(city)  # Output: New York

    # Update JSON file externally
    new_data = {'name': 'Bob', 'age': 30, 'city': 'San Francisco'}
    json_helper.save_data(new_data)

    # Update variables again
    json_helper.update_variables(variable_map)
    print(name)  # Output: Bob
    print(age)   # Output: 30
    print(city)  # Output: San Francisco
"""
