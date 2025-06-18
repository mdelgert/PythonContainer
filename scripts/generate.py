from faker import Faker
import random
from notes import create_note

def generate_and_post_notes(n=10):
    fake = Faker()
    for _ in range(n):
        title = fake.sentence(nb_words=random.randint(2, 6))
        content = fake.paragraph(nb_sentences=random.randint(2, 8))
        note = create_note(title, content)
        print(f"Created note: {note['id']} - {note['title']}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate and POST fake notes.")
    parser.add_argument("-n", "--number", type=int, default=10, help="Number of notes to generate.")
    args = parser.parse_args()
    generate_and_post_notes(args.number)

#python3 scripts/generate_fake_notes.py -n 20