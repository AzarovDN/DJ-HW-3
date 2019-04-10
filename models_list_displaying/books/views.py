from django.views import generic
from .models import Book
from .converters import PubDateConverter


class BookListView(generic.ListView):
    model = Book


class PaginatorListView(BookListView):

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        date = self.kwargs["date"]
        context['filter_date'] = date
        book_list = list(Book.objects.order_by('pub_date'))
        date_set = set()
        converter = PubDateConverter()

        for book in book_list:
            date_set.add(book.pub_date)
        date_list = sorted(list(date_set))
        index_filter_date = date_list.index(converter.to_python(date))

        if index_filter_date != 0:
            context['previous_date'] = converter.to_url(date_list[index_filter_date - 1])
        if index_filter_date != (len(date_list) - 1):
            context['next_date'] = converter.to_url(date_list[index_filter_date + 1])

        return context

    def get_queryset(self):

        if self.kwargs:
            return Book.objects.filter(pub_date=f'{self.kwargs["date"]}')

        return Book.objects.all()

    pass


