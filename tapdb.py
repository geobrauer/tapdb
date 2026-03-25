import sys
import sqlite3
import random
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPlainTextEdit, 
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout,
    QWidget
)
from tapdb_review import ReviewWindow
from tapdb_styling import styling, wrap_style, md

class InputWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.sql_input = QPlainTextEdit()
    
    self.button_review = QPushButton("Review")
    self.button_review.clicked.connect(self.execute_review)
    self.button_edit = QPushButton("Edit")
    self.button_study = QPushButton("Study")

    layout = QVBoxLayout()
    layout.addWidget(self.sql_input)
    button_layout = QHBoxLayout()
    button_layout.addWidget(self.button_study)
    button_layout.addWidget(self.button_edit)
    button_layout.addWidget(self.button_review)
    layout.addLayout(button_layout)

    container = QWidget()
    container.setLayout(layout)

    self.setCentralWidget(container)

  def execute_review(self):
    query = self.sql_input.toPlainText()
    
    try:
      with sqlite3.connect('file:/home/prime/pkm/data.db?mode=ro', uri=True) as conn:
        # register formatting functions: (SQL_NAME, ARG_COUNT, PYTHON_FUNCTION)
        conn.create_function("deva", -1, lambda text: wrap_style(text, "deva"))
        conn.create_function("gr", -1, lambda text: wrap_style(text, "greek"))
        conn.create_function("cyr", -1, lambda text: wrap_style(text, "cyr"))
        conn.create_function("han", -1, lambda text: wrap_style(text, "hanzi"))
        conn.create_function("md", -1, lambda text: md(text, "markdown"))
        cursor = conn.cursor()
        cursor.execute(query)
        self.deck = cursor.fetchall()
        random.shuffle(self.deck)

        if not self.deck:
          print("no cards found")
        else:
          self.launch_review()
    except sqlite3.Error as e:
      print(f"sqlite error: {e}")
    except Exception as e:
      print(f"app error: {e}")

  def launch_review(self):
    self.review_screen = ReviewWindow(self.deck, self)
    self.review_screen.show()
    self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputWindow()
    window.show()
    sys.exit(app.exec())
