from app import app
from unittest import TestCase
from flask import session

class ColorViewsTestCase(TestCase):

    def test_color_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)  # Adjusted to match your HTML template

    def test_color_submit(self):
        with app.test_client() as client:
            res = client.post('/fav-color', data={'color': 'blue'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>Woah! I like blue, too</h3>', html)  # Adjusted to match your HTML template

    def test_redirect(self):
        with app.test_client() as client:
            res = client.get('/redirect-me')

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')

    def test_redirection_follow(self):
        with app.test_client() as client:
            res = client.get('/redirect-me', follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Color Form</h1>', html)  # Adjusted to match your HTML template

    def test_session_count(self):
        with app.test_client() as client:
            res = client.get('/')
            with client.session_transaction() as sess:
                self.assertEqual(sess.get('count'), 1)  # Check session value

    def test_session_count_multiple(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['count'] = 999
            res = client.get('/')
            with client.session_transaction() as sess:
                self.assertEqual(sess.get('count'), 1000)  # Check session value
