# 🧩 Flask Sudoku Solver

A lightweight web application built with Python and Flask that solves standard $9 \times 9$ Sudoku puzzles using a recursive backtracking algorithm.

---

## 🚀 Features

- **Backtracking Algorithm:** Efficiently navigates empty cells, checks constraint validity (row, column, and $3 \times 3$ sub-grid), and backtracks upon invalid paths.
- **RESTful API Endpoint:** Accepts board states via JSON requests and returns solved configurations.
- **Clean Architecture:** Decoupled solver logic and web routing.

---

## 📁 Project Structure

```text
sudoku-solver/
│
├── app.py              # Flask server and backtracking algorithm
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
│
├── templates/
│   └── index.html      # Frontend UI for the Sudoku grid
│
└── static/             # Optional: CSS styles and JavaScript scripts
    ├── css/
    └── js/
