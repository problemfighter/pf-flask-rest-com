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


def test__query_data_list():
    response = requests.get(BASE_URL + "query-data-list?age=7&name=hmtmcse.com&name=problemfighter.com&name=banglafighter.com")
    response_data = response.json()

    assert response.status_code == 200, "Should be 200"
    assert isinstance(response_data["name"], list)


if __name__ == '__main__':
    test__query_data()
    test__get_query_data_value()
    test__query_data_list()
