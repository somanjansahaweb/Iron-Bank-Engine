🏦 The Iron Bank (CLI Banking System)

### A Secure, Persistent Banking Simulation Backend built with Python.

This project simulates the core functionalities of a banking system, focusing on **state persistence**, **secure authentication**, and **financial risk controls**. Unlike basic scripts, The Iron Bank maintains user data across sessions using a file-based database architecture.

---

## 🚀 Key Features

### 1. 🔐 Secure Authentication Layer
- Implementation of a login system requiring email and password verification.
- Robust **User Registration Flow** with password strength validation (min 8 chars).
- Prevents unauthorized access to banking functions.

### 2. 💾 Persistent State Management (File I/O)
- **Auto-Healing Initialization:** The system automatically checks for missing database files (`balance.txt`, `transaction_log.txt`) on startup and creates them if needed to prevent crashes.
- **Real-Time Updates:** Account balance is read from and written to disk instantly after every transaction, ensuring no data loss.

### 3. 🛡️ Risk Management & Error Handling
- **Overdraft Protection:** Logic guards prevent withdrawals exceeding the current balance.
- **Input Sanitization:** Uses `try-except` blocks to handle non-numeric inputs gracefully without crashing the application.
- **Negative Value Guards:** Prevents malicious inputs (e.g., depositing negative money).

### 4. 📜 Compliance & Audit Trail
- Includes a dedicated `log_transaction()` module.
- Records every Deposit and Withdrawal with a **Timestamp** (`YYYY-MM-DD HH:MM:SS`) to a permanent log file, simulating real-world banking compliance standards.

---

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Modules:** `os` (File System), `datetime` (Timestamping)
- **Concepts:** Functions, File Handling, Exception Handling, Control Flow, String Manipulation.
