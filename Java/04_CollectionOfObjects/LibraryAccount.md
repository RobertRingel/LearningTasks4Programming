Topic: storing objects in collections

## Learning Task: Library Account

Given is the following Java class LibraryAccount. The related [class Book](../02_ExtensionInterface/Book.java) is available in this task repository.  Read and run the code to obtain an understanding.  

Complete or change the implementation of this class in the following to meet the following requirements:  

- the printBookList-method shall print every book that is currently stored in the user's checked-out book list.  

- the checkOut-method shall guarantee that the Book b is not null and that the user can never have checked-out more than a certain number of books (LIMIT value). In such a situation the method shall return false and the book will not be checked-out. Otherwise the book will be checked-out and the method will reurn true.  

- the bringBack-method shall check whether the name and the author of the given book are equal to one of the books the user has checked-out. This will ensure the given book was really checked-out by the user. Only if the name-and-author-check is performed successful, the book will be removed from the user's checked-out book list. In this case the method will return true.  

Test your implementation with help of the given main-method.

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o2.Book;
import org.htwd.pool.o3.Person;

import java.util.ArrayList;

public class LibraryAccount {

    private Person user;
    private ArrayList<Book> books = new ArrayList<Book>();

    public LibraryAccount(String name, String birthday) {
        user = new Person(name,birthday);
    }

    public boolean checkOut(Book b) {
        books.add(b);
        return true;
    }

    public boolean bringBack(Book book) {
        if (book != null) {
            books.remove(book);
            return true;
        }
        return false;
    }

    public void printBookList() {
        System.out.println("---" + user + ": List of books ---");
        System.out.println(books);
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

```

---------------------------------------

### Solution

``` java
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
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of the ArrayList collection classes | completion task | 2 - normal | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the ArrayList class

#### Learning Activities

1) read the given Java code
2) run the program
3) understand the individual task requirements and change the method implementation accordingly one after another
4) test the changed method implementations one after another

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5  
[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0