import requests

BASE_URL = "http://localhost:5000/notes/"


def list_notes():
    resp = requests.get(BASE_URL)
    resp.raise_for_status()
    return resp.json()


def create_note(title, content):
    data = {"title": title, "content": content}
    resp = requests.post(BASE_URL, json=data)
    resp.raise_for_status()
    return resp.json()


def get_note(note_id):
    resp = requests.get(f"{BASE_URL}{note_id}")
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def update_note(note_id, title, content):
    data = {"title": title, "content": content}
    resp = requests.put(f"{BASE_URL}{note_id}", json=data)
    resp.raise_for_status()
    return resp.json()


def delete_note(note_id):
    resp = requests.delete(f"{BASE_URL}{note_id}")
    if resp.status_code == 404:
        return False
    resp.raise_for_status()
    return True


if __name__ == "__main__":
    # Example usage
    print("Creating note...")
    note = create_note("Test Note", "This is a test.")
    print("Created:", note)

    print("Listing notes...")
    notes = list_notes()
    print(notes)

    print("Getting note by ID...")
    note_id = note['id']
    note_data = get_note(note_id)
    print(note_data)

    print("Updating note...")
    updated = update_note(note_id, "Updated Title", "Updated content.")
    print(updated)

    print("Deleting note...")
    deleted = delete_note(note_id)
    print("Deleted:", deleted)

    print("Final notes list:")
    print(list_notes())
