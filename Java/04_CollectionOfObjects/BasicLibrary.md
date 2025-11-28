Topic: storing objects in collections

## Learning Task: Basic Library

The given Java class Library represents a very basic model of a library. It is based on a collection of objects of the class [LibraryAccount](LibraryAccount.java)

Read, understand and run the given class.

Complete the implementation of the methods addUser and deleteUser as follows:
- addUser: perform a check, whether the user to be added is already stored in the library - return false in that case
- deleteUser: check for an empty book list before the user gets deleted; do not delete the user in this case; return false in this case; the class LibraryAccount needs to adapted for this task

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o2.Book;

import java.util.ArrayList;
import java.util.HashMap;

public class Library {

    HashMap<String, LibraryAccount> users = new HashMap<String, LibraryAccount>();

    public Library() {}

    public boolean addUser(String name, String birthday) {
        LibraryAccount a = new LibraryAccount(name, birthday);
        users.put(name, a);
        return true;
    }

    public boolean deleteUser(String name) {
        LibraryAccount a = users.get(name);
        if (a == null)
            return false;  // user does not exist
        users.remove(name);   
        return true;
    }

    public LibraryAccount getUserAccount(String name) {
        return users.get(name);
    }

    public void showUserAccount(String name) {
        LibraryAccount a = users.get(name);
        a.printBookList();
    }

    public ArrayList<String> getAllUserNames() {
        ArrayList<String> names = new ArrayList<String>(users.keySet());
        return names;
    }

    public static void main(String[] args) {
        Book b1 = new Book("Pride and Prejudice", "Jane Austen");
        Library lib = new Library();
        boolean res = lib.addUser("Liz", "23/07/2009");
        System.out.println(res);
        res = lib.addUser("Liz", "24/07/2009");
        System.out.println(res);
        res = lib.addUser("Mark", "13/04/2010");
        System.out.println(res);
        lib.showUserAccount("Mark");
        LibraryAccount acc = lib.getUserAccount("Mark");
        acc.checkOut(b1);
        lib.showUserAccount("Mark");
        lib.deleteUser("Mark");
        res = lib.getAllUserNames().contains("Mark");
        System.out.println(res);
    }
}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o2.Book;

import java.util.ArrayList;
import java.util.HashMap;

public class Library {

    HashMap<String, LibraryAccount> users = new HashMap<String, LibraryAccount>();
    
    ...

    public boolean addUser(String name, String birthday) {
        if (users.keySet().contains(name))     
            return false; // Person already exists
        LibraryAccount a = new LibraryAccount(name, birthday);
        users.put(name, a);
        return true;
    }

    public boolean deleteUser(String name) {
        LibraryAccount a = users.get(name);
        if (a == null)
            return false;  // user does not exist
        
        if (a.getBookCount() > 0)
            return false;  // user still has books

        users.remove(name);     
        return true;
    }

    ...
}

public class LibraryAccount {

    private Person user;
    private ArrayList<Book> books = new ArrayList<Book>();
    public static final int LIMIT = 5;

    ...
    public int getBookCount() {  // this method needs to be added!
        return books.size();
    }
    ...
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of the ArrayList and HashMap collection classes | completion task | 2 - normal | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the ArrayList and HashMap classes

#### Learning Activities

1) read and run the given class to obtain understanding
2) understand the requested features of the task
3) adapt the implementation of the requested methods to implement the named features
4) add the required method in class LibraryAccount
5) test the adapted class code

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5  
[tutorialspoint.com: Java - HashMap](https://www.tutorialspoint.com/java/util/java_util_hashmap.htm)  
[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 7, pages 211-232

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0
