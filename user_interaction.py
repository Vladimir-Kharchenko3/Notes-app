from datetime import datetime

from Main import NoteManager


def main():
    note_manager = NoteManager("notes.json")
    while True:
        print("1. Add a note")
        print("2. List notes")
        print("3. Update a note")
        print("4. Delete a note")
        print("5. Filter notes by date")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            note_manager.add_note(title, body)
            print("Note added successfully!")
        
        elif choice == "2":
            notes = note_manager.load_notes()
            for note in notes:
                print(f"ID: {note.note_id}, Title: {note.title}, Body: {note.body}, Created At: {note.created_at}")
        
        elif choice == "3":
            note_id = int(input("Enter note ID to update: "))
            title = input("Enter new title (leave empty to keep current): ")
            body = input("Enter new body (leave empty to keep current): ")
            note_manager.update_note_by_id(note_id, title, body)
            print("Note updated successfully!")
        
        elif choice == "4":
            note_id = int(input("Enter note ID to delete: "))
            note_manager.delete_note_by_id(note_id)
            print("Note deleted successfully!")
        
        elif choice == "5":
            start_date_str = input("Enter start date (YYYY-MM-DD): ")
            end_date_str = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.fromisoformat(start_date_str) if start_date_str else None
            end_date = datetime.fromisoformat(end_date_str) if end_date_str else None
            filtered_notes = note_manager.filter_notes_by_date(start_date, end_date)
            for note in filtered_notes:
                print(f"ID: {note.note_id}, Title: {note.title}, Body: {note.body}, Created At: {note.created_at}")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()