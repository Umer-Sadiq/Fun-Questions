from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello world!"

# Endpoint for summing list of numbers
@app.route('/sumList', methods=['POST'])
def sum_numbers_list():
    try:
        # GET JSON object from sumList request
        data = request.get_json()

        if len(data) != 1:
            return jsonify({'error': 'Invalid input. Expected only one list of numbers.'}), 400

        key_list = list(data.keys())

        # Get the list of numbers from the input JSON
        numbers = data[key_list[0]]

        if not isinstance(numbers, list):
            return jsonify({'error': 'Invalid input. Expected a list of numbers.'}), 400

        # Sum of all the numbers
        total = sum(numbers)
        response = {'sum': total}
        
        # Return the result as a JSON response
        return jsonify(response), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/concatenate', methods=['POST'])
def concatenate_strings():
    try:
        # Extract JSON data from request
        data = request.get_json()
        #print(len(data))

        if len(data) != 2:
            raise ValueError('Input JSON should contain two strings.')
        
        keys_list = list(data.keys())
        # Extract string1 and string2 from JSON data
        string1 = data[keys_list[0]]
        string2 = data[keys_list[1]]

        # Check if string1 and string2 are strings
        if not isinstance(string1, str) or not isinstance(string2, str):
            raise ValueError('Input data is not valid strings.')

        # Concatenate the strings
        result = string1 + string2
        response = {'concatenated_result': result}

        return jsonify(response)

    except ValueError as e:
        # Handle invalid input errors
        return jsonify({'error': str(e)}), 400

if (__name__ == '__main__'):
    app.run()