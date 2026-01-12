# CRUD Opertaions

## Create Operation

Command:

> > > from bookshelf.models import Book
> > > book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
> > > print(book)

Output:
1984 by George Orwell

## Retrieve Operation

Command:

> > > retrieved_book = Book.objects.get(title="1984")
> > > print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

Output:
1984 George Orwell 1949

## Update Operation

Command:

> > > book.title = "Nineteen Eighty-Four"
> > > book.save()
> > > print(book.title)

Output:
Nineteen Eighty-Four

## Delete Operation

Command:

> > > book.delete()
> > > all_books = Book.objects.all()
> > > print(all_books)

Output:
<QuerySet []>
