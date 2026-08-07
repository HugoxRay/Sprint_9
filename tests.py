import pytest
from main import BooksCollector
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBookСollector:
# Добавление книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', [
        '',
        'A' * 100,
        'A' * 41
    ])

    def test_add_new_book_invalid_name_not_added(self, name):
    # Неккоректное название: книга не добавлена
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate_not_added(self):
    # Дубликат книги: книга не добавлена
        collector = BooksCollector()
        collector.add_new_book('Программирование')
        collector.add_new_book('Программирование')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_no_genre_by_default(self):
    # По умолчанию у книги нет жанра: пустая строка
        collector = BooksCollector()
        collector.add_new_book('Одисея')
        assert collector.get_book_genre('Одисея') == ''

# Установка жанра
    def test_set_book_genre_success(self):
    # Успешное назначение жанра существующей книге
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize('name, genre', [
        ('Несущесвтующая книга', 'Фантастика'),
        ('Дюна', 'Несуществующий жанр')
    ])

    def test_set_book_genre_invalid_book_or__genre_not_set(self, name, genre):
    # Книга не существует: жанр не устанавливается
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre('Дюна') == ''

# Поиск по жанру
    def test_get_book_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Война миров')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Война миров', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна','Война миров']
       

    def test_get_book_with_specific_genre_invalid_genre_returns_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедия') == []

# Детские книги
    @pytest.mark.parametrize('genre', ['Ужасы','Детективы'])
    def test_get_books_for_choldren_ex_age_restrict(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', genre)
        assert 'Страшная книга' not in collector.get_books_for_children()

    def test_get_book_for_children_inc_safe_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Винни-Пух')
        collector.add_new_book('Оно')
        collector.set_book_genre('Винни-Пух', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Винни-Пух']

    def test_get_book_for_children_skip_books_without_genre(self):
            collector = BooksCollector()
            collector.add_new_book('Без жанра')
            assert collector.get_books_for_children() == []

# Избранное
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Программирование')
        collector.add_book_in_favorites('Программирование')
        assert collector.get_list_of_favorites_books() == ['Программирование']

    def test_add_book_in_favorites_not_in_books_genre_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Программирование')
        collector.add_book_in_favorites('Программирование')
        collector.add_book_in_favorites('Программирование')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Программирование')
        collector.add_book_in_favorites('Программирование')
        collector.delete_book_from_favorites('Программирование')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_not_in_list(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == []
