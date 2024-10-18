def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>UrlShortener</title>' in response.data

def test_shorten_url_valid(client):
    response = client.post('/', data={'original_url': 'http://example.com'})
    assert response.status_code == 200
    assert b'Shortened link' in response.data

def test_shorten_url_invalid(client):
    response = client.post('/', data={'original_url': 'invalid-url'})
    assert response.status_code == 400