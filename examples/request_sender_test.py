import requests

BASE_URL = "http://127.0.0.1:5000/"


def test__query_data():
    response = requests.get(BASE_URL + "query-data?name=hmtmcse.com&age=7")
    response_data = response.json()

    assert response.status_code == 200, "Should be 200"
    assert response_data["name"] == "hmtmcse.com"
    assert response_data["age"] == "7"


def test__get_query_data_value():
    response = requests.get(BASE_URL + "get-query-data-value?name=hmtmcse.com&age=7")
    response_data = response.json()

    assert response.status_code == 200, "Should be 200"
    assert response_data["name"] == "hmtmcse.com"
    assert response_data["age"] == "7"
    assert response_data["noData"] == "noData"


if __name__ == '__main__':
    test__query_data()
    test__get_query_data_value()
