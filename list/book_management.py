# 도서 정보를 저장하는 클래스
class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"


# 단순 연결 리스트의 노드 클래스
class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next


# 단순 연결 리스트 클래스
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, book):
        new_node = Node(book)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = new_node

    def delete_by_title(self, title):
        current = self.head
        prev = None
        while current is not None:
            if current.data.title == title:
                if prev is None:
                    self.head = current.link
                else:
                    prev.link = current.link
                return current.data
            prev = current
            current = current.link
        return None

    def find_by_title(self, title):
        current = self.head
        while current is not None:
            if current.data.title == title:
                return current.data
            current = current.link
        return None

    def display(self):
        current = self.head
        if self.is_empty():
            print("현재 등록된 도서가 없습니다.")
        else:
            print("현재 등록된 도서 목록:")
            while current is not None:
                print(current.data)
                current = current.link


# 도서 관리 시스템 클래스
class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        book = Book(book_id, title, author, year)
        self.books.insert(book)
        print(f"도서 '{title}'가 추가되었습니다.")

    def remove_book(self, title):
        removed_book = self.books.delete_by_title(title)
        if removed_book:
            print(f"책 제목 '{title}'의 도서가 삭제되었습니다.")
        else:
            print("도서를 찾을 수 없습니다.")

    def search_book(self, title):
        book = self.books.find_by_title(title)
        if book:
            print(book)
        else:
            print("도서를 찾을 수 없습니다.")

    def display_books(self):
        self.books.display()

    def run(self):
        while True:
            print("\n=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")

            menu_selection = input("메뉴를 선택하세요: ")

            if menu_selection == '1':
                book_id = input("책 번호를 입력하세요: ")
                title = input("책 제목을 입력하세요: ")
                author = input("저자를 입력하세요: ")
                year = input("출판 연도를 입력하세요: ")
                self.add_book(book_id, title, author, year)

            elif menu_selection == '2':
                title = input("삭제할 책 제목을 입력하세요: ")
                self.remove_book(title)

            elif menu_selection == '3':
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)

            elif menu_selection == '4':
                self.display_books()

            elif menu_selection == '5':
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 다시 선택하세요.")


# 프로그램 실행
if __name__ == "__main__":
    system = BookManagement()
    system.run()
