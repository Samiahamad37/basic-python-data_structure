from datetime import datetime

class Library:
    books = {}
    
    def __init__(self, book_name, author, issue_date=None):
        self.book_name = book_name
        self.author = author
        self.issue_date = issue_date
        Library.books[book_name] = {'author': author, 'issued': False, 'issue_date': None}
        
    def check_book(self):
        if self.book_name in Library.books:
            print(f"{self.book_name} is in the library.")
        else:
            print(f"{self.book_name} is not available.")
    
    def issue(self):
        if self.book_name in Library.books and not Library.books[self.book_name]['issued']:
            Library.books[self.book_name]['issued'] = True
            Library.books[self.book_name]['issue_date'] = datetime.now().strftime('%Y-%m-%d')
            print(f"You have successfully issued {self.book_name} by {self.author} on {Library.books[self.book_name]['issue_date']}.")
        else:
            print("Issue denied. Either the book is not in the library or is already issued.")
    
    def return_book(self):
        if self.book_name in Library.books and Library.books[self.book_name]['issued']:
            Library.books[self.book_name]['issued'] = False
            Library.books[self.book_name]['issue_date'] = None
            print(f"{self.book_name} has been successfully returned.")
        else:
            print("Return denied. Either the book was not issued or does not exist in the library.")
    
# Example usage:
obj1 = Library("Mabala", "Nyamabali", 4/2/2025)
obj1.check_book()
obj1.issue()
obj1.return_book()
obj2 = Library("MABALA", 'NYAMBALI')
obj2.issue()