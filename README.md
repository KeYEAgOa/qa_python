# qa_python

Список тест функций для класса BooksCollector: 

* тест для init метода класса, проверяем что элементы класса books_rating и favorites инициализированы
`test_init_elements_of_class_not_null()`
* тест что одну и ту же книгу можно добавить только один раз
`test_add_new_book_the_same_book_possible_add_only_one_time()`
* тест что по умолчанию рейтинг для книги присваивается 1 
`test_get_book_rating_default_rating_is_one()`
* тест функции get_book_rating что у не добавленной книги нет рейтинга.
`test_get_book_rating_get_rating_for_absent_book_in_dict_result_none()`
* тест что нельзя выставить рейтинг книге, которой нет в списке 
`test_set_book_rating_set_rating_for_absent_book_in_dict_not_possible()`
* тест на граничные значения, проверяем что нельзя установить рейтинг меньше 1 и больше 10
`test_set_book_rating_only_in_range_one_and_ten_is_possible()`
* тест для списка книг с определенным рейтингом
`test_get_books_with_specific_rating_for_two_books_with_rating_five()`
* тест функции получения текущего словаря books_rating
`test_get_books_rating_for_four_books()`
* тест функции добавления книги в Избранное, добавляем в список две книги
`test_add_book_in_favorites_add_two_books()`
* тест функции добавления книги в Избранное, возможно добавить только книгу из books_rating
`test_add_book_in_favorites_add_book_from_books_rating_only_possible()`
* тест функции удаления книги из Избранного, удаление одной книги
`test_add_book_in_favorites_delete_one_book()`
* тест функции получения списка Избранных книг, получение списка из двух книг
`test_get_list_of_favorites_books_get_two_books()`

