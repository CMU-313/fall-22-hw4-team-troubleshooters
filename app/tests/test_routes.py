from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_expected_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?G1=0&G2=0&studytime=1&absences=0&freetime=1&failures=0'

    response = client.get(url)
    assert response.status_code == 200
    assert 0 <= response.json["prediction"] <= 1

def test_invalid_input_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    #missing one variable
    url = '/predict?G2=0&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 400

    url = '/predict?G1=0&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 400

    url = '/predict?G1=0&G2=0&studytime=1&absences=0&freetime=1'
    response = client.get(url)
    assert response.status_code == 400

    #first check input number before out of range
    url = '/predict?G1=0&G2=0&studytime=1&absences=0&freetime=0'
    response = client.get(url)
    assert response.status_code == 400

    #multiple missing inputs
    url = '/predict?G1=0&G2=0&studytime=1'
    response = client.get(url)
    assert response.status_code == 400


def test_out_range_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    #G1 out of bounds
    url = '/predict?G1=-1&G2=0&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    url = '/predict?G1=21&G2=0&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    #G1 out of bounds
    url = '/predict?G1=-1&G2=0&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    url = '/predict?G1=21&G2=0&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    #G2 out of bounds
    url = '/predict?G1=0&G2=-1&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    url = '/predict?G1=0&G2=21&studytime=1&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    #studytime out of bounds
    url = '/predict?G1=0&G2=0&studytime=0&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    url = '/predict?G1=0&G2=0&studytime=5&absences=0&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    #absences out of bounds
    url = '/predict?G1=0&G2=0&studytime=1&absences=-1&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    url = '/predict?G1=0&G2=0&studytime=1&absences=94&freetime=1&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    #freetime out of bounds
    url = '/predict?G1=0&G2=0&studytime=1&absences=0&freetime=0&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    url = '/predict?G1=0&G2=0&studytime=1&absences=0&freetime=6&failures=0'
    response = client.get(url)
    assert response.status_code == 405

    #failures out of bounds
    url = '/predict?G1=0&G2=0&studytime=1&absences=0&freetime=1&failures=-1'
    response = client.get(url)
    assert response.status_code == 405

    url = '/predict?G1=0&G2=0&studytime=1&absences=0&freetime=1&failures=5'
    response = client.get(url)
    assert response.status_code == 405