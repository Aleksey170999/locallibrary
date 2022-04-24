from django.test import TestCase
from catalog.models import Author, Book


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals('/catalog/author/1/', author.get_absolute_url().lower())


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        author = Author.objects.create(first_name="Vladimir", last_name="Nabokov")

        Book.objects.create(title='Dar', author=author)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_summary_len(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals('/catalog/book/1/', book.get_absolute_url())

    def test_book_str_method(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.title
        self.assertEquals(expected_object_name, str(book))
