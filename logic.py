from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.aliceVotes = 0
        self.bobVotes = 0
        self.charlieVotes = 0
        self.derekVotes = 0

        self.voteAlice.clicked.connect(lambda: self.vote(1, self.voteAlice))
        self.voteBob.clicked.connect(lambda: self.vote(2, self.voteBob))
        self.voteCharlie.clicked.connect(lambda: self.vote(3, self.voteCharlie))
        self.voteDerek.clicked.connect(lambda:self.vote(4, self.voteDerek))
        self.resultsButton.clicked.connect(lambda: self.tally())

    def vote(self, candidate: int, button):
        if candidate == 1:
            self.aliceVotes += 1
        if candidate == 2:
            self.bobVotes += 1
        if candidate == 3:
            self.charlieVotes += 1
        if candidate == 4:
            self.derekVotes += 1
    def tally(self):
        self.textBrowser.setText(f'Alice: {self.aliceVotes}'
                                 f'Bob: {self.bobVotes}'
                                 f'Charlie: {self.charlieVotes}'
                                 f'Derek: {self.derekVotes}')





