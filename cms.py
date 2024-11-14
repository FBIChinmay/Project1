class Content:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\n"

import os
import json

class CMS:
    def __init__(self, data_file):
        self.data_file = data_file
        self.contents = self.load_contents()

    def load_contents(self):
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, 'r') as file:
            contents_data = json.load(file)
            return [Content(**data) for data in contents_data]

    def save_contents(self):
        with open(self.data_file, 'w') as file:
            json.dump([content.__dict__ for content in self.contents], file, indent=4)

    def add_content(self, content):
        self.contents.append(content)
        self.save_contents()

    def update_content(self, content_id, new_title, new_body):
        for content in self.contents:
            if content.id == content_id:
                content.title = new_title
                content.body = new_body
                self.save_contents()
                return True
        return False

    def delete_content(self, content_id):
        self.contents = [content for content in self.contents if content.id != content_id]
        self.save_contents()

    def view_contents(self):
        return [str(content) for content in self.contents]


def main():
    cms = CMS('cms_data.json')

    while True:
        print("\nCustom Content Management System")
        print("1. Add Content")
        print("2. View All Contents")
        print("3. Update Content")
        print("4. Delete Content")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter content ID: ")
            title = input("Enter content title: ")
            body = input("Enter content body: ")
            content = Content(id, title, body)
            cms.add_content(content)
            print("Content added successfully.")

        elif choice == '2':
            contents = cms.view_contents()
            for content in contents:
                print(content)

        elif choice == '3':
            id = input("Enter the ID of the content to update: ")
            new_title = input("Enter new content title: ")
            new_body = input("Enter new content body: ")
            if cms.update_content(id, new_title, new_body):
                print("Content updated successfully.")
            else:
                print("Content not found.")

        elif choice == '4':
            id = input("Enter the ID of the content to delete: ")
            cms.delete_content(id)
            print("Content deleted successfully.")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()