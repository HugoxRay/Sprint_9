Тесты для BooksCollector
# Требования: 
Python 3.6, pytest
# Запуск: 
pytest -v tests.py

Содержит набор автоматических тестов для класса 'BooksCollector' из модуля: 
# main.py

Класс 'BooksCollector' имеет функционал для управления коллекцией книг:
- Добавление новых книг
- Установка жанра для книг
- Поиск книг по жанру
- Получение списка детских книг
- Управление списком избранных книг

Тесты
## Добавление книги
- test_add_new_book_add_two_books - Добавление 2х книг 
- test_add_new_book_invalid_name_not_added - Невалидные данные
- add_new_book_duplicate_not_added - Добавление дубликата
- test_add_new_book_no_genre_by_default - Проверка значения жанра по умолчанию
## Установка жанра
- test_set_book_genre_success - Назначение жанра существующей книге
- test_set_book_genre_invalid_book_or_not_set - Проверка установки жанра для несуществующей книги или невалидного жанра
## Поиск по жанру
- test_get_book_with_specific_genre_returns_correct_books - Проверка поиска по жанру
- test_get_book_with_specific_genre_invalid_genre_returns_empty - Проверка возврата пустого списка при назначении невалидного жанра
## Десткие книги
- test_get_books_for_choldren_ex_age_restrict - Проверка ограничения жанров не для детей
- test_get_book_for_children_inc_safe_genre - Проверка жанра для детей
- test_get_book_for_children_skip_books_without_genre - Проверка ограничений для книг без жанра
## Избранное
- test_add_book_in_favorites_success -Добавить книгу
- test_add_book_in_favorites_not_in_books_genre_not_added - Проверка несуществующая книга не добавляется в избранное
- test_add_book_in_favorites_duplicate_not_added - Добавление дубликата
- test_delete_book_from_favorites_success - Удаление

В тестах используется параметризация:
# @pytest.mark.parametrize
- Проверяет граничные значения
# test_add_new_book_invalid_name_not_added
- Тестирует различные жанры 
# test_add_new_book_invalid_name_not_added
