from rest_framework.test import APITestCase
from .models import Note

class NoteTests(APITestCase):
    def test_create_note(self):
        response = self.client.post('/api/notes/', {'title': 'Test', 'body': 'Test Body'})
        self.assertEqual(response.status_code, 201)

    def test_fetch_note_by_id(self):
        note = Note.objects.create(title='Test', body='Test Body')
        response = self.client.get(f'/api/notes/{note.id}/')
        self.assertEqual(response.status_code, 200)

    def test_query_notes_by_title(self):
        Note.objects.create(title='Test', body='Test Body')
        response = self.client.get('/api/notes/', {'title': 'Test'})
        self.assertEqual(response.status_code, 200)

    def test_update_note(self):
        note = Note.objects.create(title='Test', body='Test Body')
        response = self.client.put(f'/api/notes/{note.id}/', {'title': 'Updated', 'body': 'Updated Body'})
        self.assertEqual(response.status_code, 200)
