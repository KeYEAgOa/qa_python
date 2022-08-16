from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
# add data for commit
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тест для init метода класса, проверяем что элементы класса books_rating и favorites не None
    # то есть были инициализированы после создания класса
    def test_init_elements_of_class_not_null(self):
        bc = BooksCollector()
        assert bc.books_rating != None and bc.favorites != None

    # тест что одну и ту же книгу можно добавить только один раз
    def test_add_new_book_the_same_book_possible_add_only_one_time(self):
        bc = BooksCollector()
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(bc.get_books_rating()) == 1

    # тест что по умолчанию рейтинг для книги присваивается 1
    def test_get_book_rating_default_rating_is_one(self):
        bc = BooksCollector()
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert bc.get_book_rating('Что делать, если ваш кот хочет вас убить') == 1

    # тест get_book_rating что у не добавленной книги нет рейтинга.
    def test_get_book_rating_get_rating_for_absent_book_in_dict_result_none(self):
        bc = BooksCollector()
        assert bc.get_book_rating('Что делать, если ваша собака хочет вас убить') == None

    # тест что нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_set_rating_for_absent_book_in_dict_not_possible(self):
        bc = BooksCollector()
        bc.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        assert bc.get_book_rating('Что делать, если ваш кот хочет вас убить') == None

    # тест на граничные значения, проверяем что нельзя установить рейтинг меньше 1 и больше 10
    def test_set_book_rating_only_in_range_one_and_ten_is_possible(self):
        bc = BooksCollector()
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        bc.set_book_rating('Что делать, если ваш кот хочет вас убить',0)
        zero_rating = bc.get_book_rating('Что делать, если ваш кот хочет вас убить')
        bc.set_book_rating('Что делать, если ваш кот хочет вас убить', 11)
        eleven_rating = bc.get_book_rating('Что делать, если ваш кот хочет вас убить')
        bc.set_book_rating('Что делать, если ваш кот хочет вас убить', 10)
        ten_rating = bc.get_book_rating('Что делать, если ваш кот хочет вас убить')
        assert zero_rating == 1 and eleven_rating == 1 and ten_rating == 10

    # тест для списка книг с определенным рейтингом
    def test_get_books_with_specific_rating_for_two_books_with_rating_five(self):
        bc = BooksCollector()
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        bc.set_book_rating('Что делать, если ваш кот хочет вас убить', 3)
        bc.add_new_book('Что делать, если ваша собака хочет вас убить')
        bc.set_book_rating('Что делать, если ваша собака хочет вас убить', 5)
        bc.add_new_book('Что делать, если ваши рыбки хотят вас убить')
        bc.set_book_rating('Что делать, если ваши рыбки хотят вас убить', 5)
        bc.add_new_book('Что делать, если ваша жена хочет вас убить')
        bc.set_book_rating('Что делать, если ваша жена хочет вас убить', 7)
        assert len(bc.get_books_with_specific_rating(5)) == 2

    # тест функции получения текущего словаря books_rating
    def test_get_books_rating_for_four_books(self):
        bc = BooksCollector()
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        bc.set_book_rating('Что делать, если ваш кот хочет вас убить', 3)
        bc.add_new_book('Что делать, если ваша собака хочет вас убить')
        bc.set_book_rating('Что делать, если ваша собака хочет вас убить', 5)
        bc.add_new_book('Что делать, если ваши рыбки хотят вас убить')
        bc.set_book_rating('Что делать, если ваши рыбки хотят вас убить', 5)
        bc.add_new_book('Что делать, если ваша жена хочет вас убить')
        bc.set_book_rating('Что делать, если ваша жена хочет вас убить', 7)
        assert len(bc.get_books_rating()) == 4

    # тест функции добавления книги в Избранное, добавляем в список две книги
    def test_add_book_in_favorites_add_two_books(self):
        bc = BooksCollector()
        bc.add_new_book('Гордость и предубеждение и зомби')
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        bc.add_book_in_favorites('Гордость и предубеждение и зомби')
        bc.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(bc.favorites) == 2

    # тест функции добавления книги в Избранное, возможно добавить только книгу из books_rating
    def test_add_book_in_favorites_add_book_from_books_rating_only_possible(self):
        bc = BooksCollector()
        bc.add_new_book('Гордость и предубеждение и зомби')
        bc.add_book_in_favorites('Гордость и предубеждение и зомби')
        bc.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(bc.favorites) == 1

    # тест функции удаления книги из Избранного, удаление одной книги
    def test_add_book_in_favorites_delete_one_book(self):
        bc = BooksCollector()
        bc.add_new_book('Гордость и предубеждение и зомби')
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        bc.add_book_in_favorites('Гордость и предубеждение и зомби')
        bc.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        bc.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(bc.favorites) == 1

    # тест функции получения списка Избранных книг, получение списка из двух книг
    def test_get_list_of_favorites_books_get_two_books(self):
        bc = BooksCollector()
        bc.add_new_book('Гордость и предубеждение и зомби')
        bc.add_new_book('Что делать, если ваш кот хочет вас убить')
        bc.add_book_in_favorites('Гордость и предубеждение и зомби')
        bc.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(bc.get_list_of_favorites_books()) == 2



