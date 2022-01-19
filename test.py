from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
    
    def test_homepage(self):
        with self.client:
            response = self.client.get('/')
            self.assertIn("board", session)
            self.assertIsNone(session.get("highscore"))
            self.assertIsNone(session.get("playcount"))

    def test_word_validity(self):
        with self.client.session_transaction() as sesh:
            sesh["board"] = [["B", "B", "B", "B", "B"],
                             ["A", "A", "A", "A", "A"],
                             ["B", "B", "B", "B", "B"],
                             ["Y", "Y", "Y", "Y", "Y"],
                             ["Y", "Y", "Y", "Y", "Y"]]
        response = self.client.get("/check-word?word=baby")
        self.assertEqual(response.json['result'], 'ok')
    
    def test_invalid_word(self):        
        self.client.get('/')
        response = self.client.get('/check-word?word=hamburger')
        self.assertEqual(response.json['result'], 'not-on-board')
    
    def non_english_word(self):    
        self.client.get('/')
        response = self.client.get(
            '/check-word?word=zzzzzzzzzzzzzzzzzz')
        self.assertEqual(response.json['result'], 'not-word')