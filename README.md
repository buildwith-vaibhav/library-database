# Library Management System

A simple **command-line Library Management System** built in Python.

Books are stored in a CSV file (`library.csv`) so data persists between runs.  
Perfect for learning file handling, CSV operations, and basic application logic.

## Features

- **Add Book** – Add a new book with ISBN, title, and author (duplicate ISBN check)
- **View All Books** – Display the complete catalogue in a clean table
- **Search Book** – Search by title or author (case-insensitive)
- **Issue Book** – Issue a book (sets status to *Issued* + calculates due date)
- **Return Book** – Return a book and automatically calculate late fine
- **Exit** – Quit the application safely

### Business Rules

| Setting          | Value          |
|------------------|----------------|
| Loan period      | 5 days         |
| Fine per day     | ₹5             |
| Data storage     | `library.csv`  |

## How to Run

### Prerequisites
- Python 3.6 or higher
- A terminal / command prompt
- Git (only if you want to clone the repository)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/buildwith-vaibhav/library-database.git
   cd library-database
   ```

2. **Verify Python is installed**
   ```bash
   python --version
   # or
   python3 --version
   ```
   You should see a version starting with `Python 3.x`.

3. **Run the application**
   ```bash
   python Library_Database.py
   # or (if python points to Python 2)
   python3 Library_Database.py
   ```

4. Use the on-screen menu (options 1–6) to interact with the system.

### Notes
- No external packages or virtual environment is required.
- The data file `library.csv` is created automatically on the first run.
- The program uses only Python’s standard library (`os`, `csv`, `datetime`).

## Sample Screenshots

### Main Menu
```
==== LIBRARY MANAGEMENT SYSTEM ====
1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Exit
Enter your choice (1-6):
```

### Add Book
```
Enter The ISBN of Book: 978-0134685991
Enter The Book Title: Effective Python
Enter The Book Author: Brett Slatkin
Book 'Effective Python' by Brett Slatkin added successfully!
```

### View All Books
```
ISBN               Title                    Author              Status      DueDate
------------------------------------------------------------------------------------------
978-0134685991     Effective Python         Brett Slatkin       Available   
978-1491946008     Fluent Python            Luciano Ramalho     Available   
978-0596009205     Head First Python        Paul Barry          Available   
```

### Search Book
```
Enter title or author to search: python

Effective Python by Brett Slatkin [Available]
Fluent Python by Luciano Ramalho [Available]
Head First Python by Paul Barry [Available]
```

### Issue Book
```
Enter ISBN to Issue: 978-0134685991
Book 'Effective Python' issued successfully!
Issue Date: 2026-08-29 | Due Date: 2026-09-03
```

## Project Structure

```
library-database/
├── Library_Database.py   # Main application
└── README.md             # This file
```

> `library.csv` is created automatically on the first run.

## Author

**Vaibhav Tiwari**  
VIT Bhopal  

---

*First-year project – Library Management System*
