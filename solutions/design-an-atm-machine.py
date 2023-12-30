class ATM:
    def __init__(self):
        self.notes_count = [0, 0, 0, 0, 0]
        self.notes = [20, 50, 100, 200, 500]
    def deposit(self, notesCount):
        for i in range(len(self.notes_count)):
            self.notes_count[i] += notesCount[i]

    def withdraw(self, amount):
        result = [0, 0, 0, 0, 0]
        remaining = amount

        for i in range(len(self.notes)-1, -1, -1):
            num_banknotes = min(remaining // self.notes[i], self.notes_count[i])
            result[i] = num_banknotes
            remaining -= num_banknotes * self.notes[i]

        if remaining == 0:
            for i in range(len(self.notes)):
                self.notes_count[i] -= result[i]
            return result
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)