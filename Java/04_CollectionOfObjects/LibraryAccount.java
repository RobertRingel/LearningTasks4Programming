package org.htwd.pool.o4;

import org.htwd.pool.o2.Book;
import org.htwd.pool.o3.Person;

import java.util.ArrayList;

public class LibraryAccount {

    private Person user;
    private ArrayList<Book> books = new ArrayList<Book>();
    public static final int LIMIT = 5;

    public LibraryAccount(String name, String birthday) {
        user = new Person(name,birthday);
    }

    public boolean checkOut(Book b) {
        if (b==null || books.size()>LIMIT)
            return false;
        books.add(b);
        return true;
    }

    public boolean bringBack(Book book) {
        String author = book.getAuthor();
        String title = book.getTitle();
        for (Book b : books) {
            if (author ==  b.getAuthor() && title == b.getTitle()) {
                books.remove(b);
                return true;
            }
        }
        return false;
    }

    public void printBookList() {
        System.out.println("---" + user + ": List of books ---");
        for (Book b : books)
            System.out.println(b);
    }

    public static void main(String[] args) {
        Book b1 = new Book("Pride and Prejudice", "Jane Austen");
        Book b2 = new Book("Tom Sawyer", "Mark Twain");
        LibraryAccount libacc = new LibraryAccount("Liz", "23/07/2009");
        libacc.checkOut(b1);
        libacc.checkOut(b2);
        libacc.bringBack(b2);
        libacc.printBookList();
    }

}
