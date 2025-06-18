class Note:
    _notes = {}
    _id = 1

    @classmethod
    def create(cls, data):
        note = {"id": cls._id, **data}
        cls._notes[cls._id] = note
        cls._id += 1
        return note

    @classmethod
    def get(cls, note_id):
        return cls._notes.get(note_id)

    @classmethod
    def get_all(cls):
        return list(cls._notes.values())

    @classmethod
    def update(cls, note_id, data):
        if note_id in cls._notes:
            cls._notes[note_id].update(data)
            return cls._notes[note_id]
        return None

    @classmethod
    def delete(cls, note_id):
        return cls._notes.pop(note_id, None)
