Topic: storing objects in collections

## Learning Task: The Family Members

Given is the following Java class FamilyMembers. Read and run the code to obtain an understanding.  

Write a brief textual description of the functionality of this class.

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o3.Person;

import java.util.ArrayList;
import java.util.HashMap;

public class FamilyMembers {
    private HashMap<String, Person> members = new HashMap<String, Person>();

    public FamilyMembers() {}

    public void addPerson(String role, Person p) {
        members.put(role, p);
    }

    public Person getPerson(String role) {
        return members.get(role);
    }

    public void removePerson(String role) {
        members.remove(role);
    }

    public ArrayList<String> getAllRoles() {
        ArrayList<String> roles = new ArrayList<String>(members.keySet());
        return roles;
    }

    public static void main(String[] args) {
        Person p1 = new Person("Sue", "21.02.2024");
        Person p2 = new Person("Bob", "17.07.2025");
        FamilyMembers f = new FamilyMembers();
        f.addPerson("Sister", p1);
        f.addPerson("Brother", p2);
        ArrayList<String> roles = f.getAllRoles();
        for (String r:roles) {
            Person p = f.getPerson(r);
            System.out.println(p);
        }

        f.removePerson("Brother");
        System.out.println(f.getPerson("Sister"));
    }
}
```

---------------------------------------

### Solution

The class is used to model a store of family members. The implementation is based on a HashMap to store [Person objects](../03_UsingObjects/Person.java) to be accessed by their role in the family. So the key to access the HashMap is a role name.  
The class provides functionality to add a Person object to the store. Using the role name one can access a stored Person object or one can remove it. Furthermore it is possible to get a list of all the role names currently used as key by the underlying HashMap.  
The main-method shows the functionality of this class.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of the HashMap and ArrayList collection classes | worked-out example | 1 - low | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the HashMap and ArrayList classes

#### Learning Activities

1) read the given Java code
2) run the program
3) write a brief description of the class functionality

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
