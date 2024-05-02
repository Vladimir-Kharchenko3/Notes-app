import json
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, created_at=None, updated_at=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def update(self, title=None, body=None):
        self.title = title if title is not None else self.title
        self.body = body if body is not None else self.body
        self.updated_at = datetime.now()

    def as_dict(self):
        return {
            "note_id": self.note_id,
            "title": self.title,
            "body": self.body,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, note_dict):
        return cls(
            note_dict["note_id"],
            note_dict["title"],
            note_dict["body"],
            datetime.fromisoformat(note_dict["created_at"]),
            datetime.fromisoformat(note_dict["updated_at"])
        )

class NoteManager:
    def __init__(self, filename):
        self.filename = filename

    def load_notes(self):
        try:
            with open(self.filename, "r") as file:
                notes_data = json.load(file)
                return [Note.from_dict(note_dict) for note_dict in notes_data]
        except FileNotFoundError:
            return []

    def save_notes(self, notes):
        with open(self.filename, "w") as file:
            notes_data = [note.as_dict() for note in notes]
            json.dump(notes_data, file, indent=4)

    def add_note(self, title, body):
        notes = self.load_notes()
        new_note_id = max([note.note_id for note in notes] + [0]) + 1
        new_note = Note(new_note_id, title, body)
        notes.append(new_note)
        self.save_notes(notes)
        return new_note

    def delete_note_by_id(self, note_id):
        notes = self.load_notes()
        notes = [note for note in notes if note.note_id != note_id]
        self.save_notes(notes)

    def update_note_by_id(self, note_id, title=None, body=None):
        notes = self.load_notes()
        for note in notes:
            if note.note_id == note_id:
                note.update(title, body)
                break
        self.save_notes(notes)

    def filter_notes_by_date(self, start_date=None, end_date=None):
        notes = self.load_notes()
        if start_date is not None:
            notes = [note for note in notes if note.created_at >= start_date]
        if end_date is not None:
            notes = [note for note in notes if note.created_at <= end_date]
        return notes