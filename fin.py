class Entry:
    def __init__(self, id, description, amount, entry_type):
        self.id = id
        self.description = description
        self.amount = amount
        self.entry_type = entry_type

    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, Amount: {self.amount}, Type: {self.entry_type}"
1
class FinanceManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def view_entries(self):
        return [str(entry) for entry in self.entries]

    def get_balance(self):
        income = sum(entry.amount for entry in self.entries if entry.entry_type == 'income')
        expenses = sum(entry.amount for entry in self.entries if entry.entry_type == 'expense')
        return income - expenses

    def get_summary(self):
        income = sum(entry.amount for entry in self.entries if entry.entry_type == 'income')
        expenses = sum(entry.amount for entry in self.entries if entry.entry_type == 'expense')
        balance = income - expenses
        return {
            "Total Income": income,
            "Total Expenses": expenses,
            "Balance": balance
        }
def main():
    manager = FinanceManager()

    while True:
        print("\nPersonal Finance Management System")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. View Balance")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter entry ID: ")
            description = input("Enter entry description: ")
            amount = float(input("Enter amount: "))
            entry_type = input("Enter type (income/expense): ").lower()
            if entry_type not in ['income', 'expense']:
                print("Invalid entry type. Please enter 'income' or 'expense'.")
                continue
            entry = Entry(id, description, amount, entry_type)
            manager.add_entry(entry)
            print("Entry added successfully.")

        elif choice == '2':
            entries = manager.view_entries()
            for entry in entries:
                print(entry)

        elif choice == '3':
            balance = manager.get_balance()
            print(f"Current Balance: {balance}")

        elif choice == '4':
            summary = manager.get_summary()
            for key, value in summary.items():
                print(f"{key}: {value}")

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()