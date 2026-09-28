import os
import csv
from datetime import datetime, timedelta

FILE_NAME = "library.csv"
FIELDS = ["ISBN", "Title", "Author", "Status", "IssueDate", "DueDate"]
LOAN_DAYS = 5
FINE_PER_DAY = 5
DATE_FORMAT = "%Y-%m-%d"


# ---------- file handling ----------
def load_book():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_books(books):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(books)


# ---------- add book ----------
def add_book():
    books = load_book()

    isbn = input("Enter The ISBN of Book: ").strip()
    if not isbn:
        print("ISBN cannot be empty.\n")
        return

    # avoid duplicate books
    for b in books:
        if b["ISBN"] == isbn:
            print("A book with this ISBN already exists.\n")
            return

    title = input("Enter The Book Title: ").strip()
    author = input("Enter The Book Author: ").strip()
    if not title or not author:
        print("Title and author cannot be empty.\n")
        return

    new_book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Status": "Available",
        "IssueDate": "",
        "DueDate": "",
    }
    books.append(new_book)
    save_books(books)
    print(f"Book '{title}' by {author} added successfully!\n")


# ---------- view all ----------
def view_all():
    books = load_book()
    if not books:
        print("No books in the library yet.\n")
        return

    print(f"\n{'ISBN':<18}{'Title':<25}{'Author':<20}{'Status':<12}{'DueDate'}")
    print("-" * 90)
    for b in books:
        print(f"{b['ISBN']:<18}{b['Title']:<25}{b['Author']:<20}{b['Status']:<12}{b['DueDate']}")
    print()


# ---------- search ----------
def search():
    books = load_book()
    query = input("Enter title or author to search: ").strip().lower()
    if not query:
        print("Please type something to search.\n")
        return

    found = False
    print()
    for b in books:
        if query in b["Title"].lower() or query in b["Author"].lower():
            print(f"{b['Title']} by {b['Author']} [{b['Status']}]")
            found = True
    if found:
        print()
    else:
        print("No matching books found.\n")


# ---------- issue ----------
def issue_book():
    books = load_book()
    isbn = input("Enter ISBN to Issue: ").strip()

    for b in books:
        if b["ISBN"] == isbn:
            if b["Status"] == "Issued":
                print("This book is already issued.\n")
                return

            today = datetime.now()
            due = today + timedelta(days=LOAN_DAYS)

            b["Status"] = "Issued"
            b["IssueDate"] = today.strftime(DATE_FORMAT)
            b["DueDate"] = due.strftime(DATE_FORMAT)

            save_books(books)
            print(f"Book '{b['Title']}' issued successfully!")
            print(f"Issue Date: {b['IssueDate']} | Due Date: {b['DueDate']}\n")
            return
    print("No book found with that ISBN.\n")


# ---------- return ----------
def calculate_fine(due_date, return_date):
    days_late = (return_date - due_date).days
    if days_late > 0:
        return days_late * FINE_PER_DAY
    return 0


def return_books():
    books = load_book()
    isbn = input("Enter ISBN to return: ").strip()

    for b in books:
        if b["ISBN"] == isbn:
            if b["Status"] != "Issued":
                print("This book was not issued.\n")
                return

            today = datetime.now().date()
            try:
                due_date = datetime.strptime(b["DueDate"], DATE_FORMAT).date()
            except (ValueError, TypeError):
                # damaged/missing due date in the CSV: treat as no fine
                due_date = today

            fine = calculate_fine(due_date, today)

            b["Status"] = "Available"
            b["IssueDate"] = ""
            b["DueDate"] = ""
            save_books(books)

            if fine > 0:
                print(f"'{b['Title']}' returned. Late by {(today - due_date).days} day(s). Fine: Rs.{fine}\n")
            else:
                print(f"'{b['Title']}' returned on time. No fine.\n")
            return
    print("No book found with that ISBN.\n")


# ---------- menu ----------
def main():
    while True:
        print("==== LIBRARY MANAGEMENT SYSTEM ====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
