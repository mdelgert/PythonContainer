from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.notes import NoteSchema
from models.notes import Note

blp = Blueprint("notes", "notes", url_prefix="/notes", description="Operations on notes")

@blp.route("/")
class NotesList(MethodView):
    @blp.response(200, NoteSchema(many=True))
    def get(self):
        return Note.get_all()

    @blp.arguments(NoteSchema)
    @blp.response(201, NoteSchema)
    def post(self, new_data):
        return Note.create(new_data)

@blp.route("/<int:note_id>")
class Notes(MethodView):
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        note = Note.get(note_id)
        if not note:
            blp.abort(404, "Note not found.")
        return note

    @blp.arguments(NoteSchema)
    @blp.response(200, NoteSchema)
    def put(self, update_data, note_id):
        note = Note.update(note_id, update_data)
        if not note:
            blp.abort(404, "Note not found.")
        return note

    @blp.response(204)
    def delete(self, note_id):
        note = Note.delete(note_id)
        if not note:
            blp.abort(404, "Note not found.")
