# review function (w/o spaced repetition)

from PyQt6.QtWidgets import QMainWindow, QTextBrowser, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
import re
import unicodedata
import markdown
import html
from tapdb_styling import styling, wrap_style

class ReviewWindow(QMainWindow):
  def __init__(self, flashcards, parent=None):
    super().__init__(parent)

    self.main_window = parent
    self.cards = flashcards    # all rows i.e. cards
    self.index = 0             # row #0, row #1
    self.is_flipped = False
    self.setMinimumSize(800, 600)

    # card content
    self.content = QTextBrowser()
    self.content.setReadOnly(True)
    self.content.setFrameStyle(0)
    self.content.document().setDefaultStyleSheet(styling)

    # cards remaining
    self.remaining = QLabel()
    self.remaining.setAlignment(Qt.AlignmentFlag.AlignRight)

    layout = QVBoxLayout()
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(10)
    layout.addWidget(self.remaining)
    layout.addWidget(self.content)

    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)

    self.update_display()

  def update_display(self):
    remaining = len(self.cards) - self.index
    if remaining > 0:
      card = self.cards[self.index]
      # sql tuples: 
      front = card[0]
      back = card[1]
      back1 = card[2] if len(card) > 2 else None
      back2 = card[3] if len(card) > 3 else None
      if self.is_flipped:
        text = self.format_back(front, back, back1, back2)
      else:
        text = self.format_front(front)
      self.content.setHtml(text)
      self.remaining.setText(f"Remaining: {remaining}")
    else:
      self.close()

  def keyPressEvent(self, event):
    if event.key() == Qt.Key.Key_Tab:
      if not self.is_flipped:
        self.is_flipped = True
        self.update_display()
      else:
        self.next_card()
    elif event.key() == Qt.Key.Key_1:
      if self.index < len(self.cards):
        card = self.cards[self.index]
        insert_pos = min(self.index + 4, len(self.cards))
        self.cards.insert(insert_pos, card)
        self.next_card()

  def next_card(self):
    self.index += 1
    self.is_flipped = False
    self.update_display()

  def closeEvent(self, event):
    if self.main_window:
      self.main_window.show()
    event.accept()

  def format_back(self, front, back, back1=None, back2=None):
    parts = [
        wrap_style(front, "front"),
        '<hr width="90%">',
        wrap_style(back, "back")
    ]

    if back1:
        parts.append(wrap_style(back1, "back_plus"))
    if back2:
        parts.append(wrap_style(back2, "back_plus"))
        
    return "".join(parts)

  def format_front(self, front):
    return wrap_style(front, "front")
