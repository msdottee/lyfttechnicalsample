from lyfttechnicalsample.app import app


def test_api_returns_split_string_on_post():
    with app.test_client() as client:
        response = client.post('/test', json={
            'string_to_cut': 'iamyourlyftdriver'
        })
        json_data = response.get_json()
        assert response.status_code == 200
        assert json_data == {'return_string': 'muydv'}


def test_api_returns_400_bad_request_for_invalid_data():
    with app.test_client() as client:
        response = client.post('/test', json={})
        assert response.status_code == 400
