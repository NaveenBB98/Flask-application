import requests

def test_get_dropdown_values():
    response = requests.get('http://localhost:5000/dropdown_values')
    data = response.json()
    dropdown1_value = data['dropdown1']
    dropdown2_value = data['dropdown2']

    # Now you can use dropdown1_value and dropdown2_value in your tests
    assert dropdown1_value == 'value1'
    assert dropdown2_value == 'value2'
