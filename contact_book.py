contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"✅ Contact '{name}' added!")

def view_contacts():
    if not contacts:
        print("📭 No contacts found!")
    else:
        print("\n📒 Your Contacts:")
        for name, phone in contacts.items():
            print(f"  👤 {name} → {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"✅ Found! {name} → {contacts[name]}")
    else:
        print(f"❌ '{name}' not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ '{name}' deleted!")
    else:
        print(f"❌ '{name}' not found!")

def main():
    print("📒 Welcome to Contact Book!")
    while True:
        print("\n--- MENU ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1-5.")

main()