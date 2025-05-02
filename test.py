from main import BooksCollector
import pytest


class TestBooksCollector:
    def test_add_new_book_success(self):
        collector = BooksCollector()
        title = 'А зори здесь тихие'
        collector.add_new_book(title)
        assert title in collector.get_books_genre()

    def test_add_new_book_name_over_41_simbols(self):
        collector = BooksCollector()
        collector.add_new_book('Рассвет полночи, или Созерцание славы, торжества и мудрости порфироносных, браноносных и мирных гениев')
        assert not collector.get_books_genre()

    def test_add_new_book_name_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert not collector.get_books_genre()

    def test_add_new_book_unsuccessfully_double_add(self):
        collector = BooksCollector()
        collector.add_new_book('А зори здесь тихие')
        collector.add_new_book('А зори здесь тихие')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Лунный камень')
        collector.set_book_genre('Лунный камень', 'Детективы')
        assert collector.get_book_genre('Лунный камень') == 'Детективы'

    def test_get_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Лунный камень')
        collector.set_book_genre('Лунный камень', 'Детективы')
        assert collector.get_book_genre('Лунный камень') == 'Детективы'

    def test_get_books_with_specific_genre_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1

    def test_get_books_genre_is_not_empty(self):
        collector = BooksCollector()
        title = 'Призрак дома на холме'
        collector.add_new_book('Призрак дома на холме')
        assert title in collector.get_books_genre()

    @pytest.mark.parametrize('books', [
        {
            'Дракула': 'Ужасы',
            'Голубая книга': 'Комедии'
        },
        {
            'Дюна': 'Фантастика',
            'Неуютная ферма': 'Комедии'
        }
    ]
                             )
    def test_get_books_for_children(self, books):
        collector = BooksCollector()
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        result = collector.get_books_for_children()
        assert all(collector.get_book_genre(item) not in collector.genre_age_rating for item in result)

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Призрак дома на холме')
        collector.add_book_in_favorites('Призрак дома на холме')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Призрак дома на холме')
        collector.add_book_in_favorites('Призрак дома на холме')
        collector.delete_book_from_favorites('Призрак дома на холме')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_in_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Призрак дома на холме')
        collector.add_book_in_favorites('Призрак дома на холме')
        assert collector.get_list_of_favorites_books()
