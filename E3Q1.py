class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # کتاب به صورت پیش‌فرض موجود است

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}'

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # لیست کتاب‌های امانت گرفته شده

    def __str__(self):
        return f'Member Name: {self.name}, Member ID: {self.member_id}'

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed "{book.title}".')
        else:
            print(f'Sorry, "{book.title}" is not available.')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f'{self.name} returned "{book.title}".')
        else:
            print(f'{self.name} did not borrow "{book.title}".')


class Library:
    def __init__(self):
        self.books = []  # لیست کتاب‌ها
        self.members = []  # لیست اعضا

    def add_book(self, book):
        self.books.append(book)
        print(f'Added book: {book.title}')

    def register_member(self, member):
        self.members.append(member)
        print(f'Registered member: {member.name}')

    def issue_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member and book:
            member.borrow_book(book)
        else:
            print('Member or book not found.')

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member and book:
            member.return_book(book)
        else:
            print('Member or book not found.')


# ایجاد کتاب‌ها
book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")

# ایجاد کتابخانه و اضافه کردن کتاب‌ها
library = Library()
library.add_book(book1)
library.add_book(book2)

# ثبت یک عضو
member = Member("آلیس", "M001")
library.register_member(member)

# امانت دادن کتاب به عضو
library.issue_book("M001", "1234567890")

# بازگرداندن کتاب
library.return_book("M001", "1234567890")

