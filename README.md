# 📊 Accounting Management System

A beginner-friendly Python project for analyzing transaction data stored in a CSV file. This project performs basic accounting calculations such as total sales, total purchases, net profit/loss, and finding the highest sale and purchase transactions.

---

## 🚀 Features

* Display all transactions
* Calculate total sales
* Calculate total purchases
* Calculate net profit or loss
* Find the highest sale transaction
* Find the highest purchase transaction
* Read transaction records from a CSV file

---

## 🛠️ Technologies Used

* Python 3
* CSV Module
* Git & GitHub

---

## 📁 Project Structure

```
Accounting/
│
├── accounting.py
├── annual_transaction_data_2025.csv
├── .gitattributes
└── README.md
```

---

## 📂 Dataset

The project uses a CSV file named:

```
annual_transaction_data_2025.csv
```

Each transaction contains:

* ID
* Date
* Month
* Transaction Type (Sale/Purchase)
* Amount

Example:

| ID       | Date       | Month   | Transaction | Amount   |
| -------- | ---------- | ------- | ----------- | -------- |
| TXN00001 | 2025-01-02 | January | Purchase    | 8573.62  |
| TXN00002 | 2025-01-05 | January | Sale        | 12000.50 |

---

## ⚙️ Functions Implemented

### `get_data()`

Reads the CSV file and stores all records in a list of dictionaries.

### `all_transactions()`

Displays every transaction.

### `total_sales()`

Calculates the total amount of all sales.

### `total_purchase()`

Calculates the total amount of all purchases.

### `net_profit_loss()`

Determines whether the business made a profit or a loss.

### `highest_sale()`

Finds the transaction with the highest sale amount.

### `highest_purchase()`

Finds the transaction with the highest purchase amount.

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/adityaaggarwal1011/Accounting.git
```

Move into the project directory:

```bash
cd Accounting
```

Run the program:

```bash
python accounting.py
```

---

## 📈 Future Improvements

* Lowest sale transaction
* Lowest purchase transaction
* Average sales and purchases
* Number of sale and purchase transactions
* Monthly sales report
* Monthly purchase report
* Search transaction by ID
* Export report to a text file
* Menu-driven interface
* Object-oriented implementation

---

## 🎯 Purpose

This project was created for learning Python programming, CSV file handling, loops, functions, and basic accounting data analysis.

---

## 👨‍💻 Author

**Aditya Aggarwal**

GitHub: https://github.com/adityaaggarwal1011

---

⭐ If you found this project useful, consider giving it a star!
