Topic: storing objects in collections

## Learning Task: My Contacts II

Given is the code of the two Java classes ContactInfo and ContactStore, whereas ContactInfo is an extension of the already known class [Person](../03_UsingObjects/Person.java).

Read and run the given code. Implement a new method to obtain a ContactInfo object by its list index.
Implement another method to print an overview of the stored contact information in a way to show the list index number and the related person name. 


**The ContactInfo class:**
``` java
package org.htwd.pool.o4; 

import org.htwd.pool.o3.Person;

public class ContactInfo extends Person {
    private String address;
    private String mobile;

    public ContactInfo(String name, String bday, String addr, String mobile) {
        super(name, bday);
        this.address = addr;
        this.mobile = mobile;
    }

    public String getAddress() { return this.address; }
    public String getMobile() { return this.mobile; }

    public String toString() {
        StringBuilder sb = new StringBuilder(super.toString());
        sb.append(" : ");
        sb.append(this.getAddress());
        sb.append(" : ");
        sb.append(this.getMobile());
        return sb.toString();
    }
}
```

``` java
package org.htwd.pool.o4;

import java.util.ArrayList;

public class ContactStore {

    private ArrayList<ContactInfo> contactList = new ArrayList<ContactInfo>();
    public ContactStore() {}

    public void addContactInfo(ContactInfo c) {
        contactList.add(c);
    }

    public ContactInfo getByName(String name) {
        for (ContactInfo c : contactList) {
            if (c.getName().equals(name))
                return c;
        }
        return null;
    }

    public boolean removeByName(String name) {
        ContactInfo c = this.getByName(name);
        if (c == null)
            return false;
        contactList.remove(c);
        return true;
    }

    public static void main(String[] args) {
        ContactInfo c1 = new ContactInfo("Max", "27/12/2004", "01243 Uphill", "---");
        ContactInfo c2 = new ContactInfo("Sue", "17/02/2007", "01244 Downunder", "---");
        ContactStore s = new ContactStore();
        s.addContactInfo(c1);
        s.addContactInfo(c2);
        ci = s.getByName("Max");
        System.out.println(ci);
        boolean b = s.removeByName("Max");
        System.out.println(b);
    }

}
```

---------------------------------------

### Solution

``` java
package org.htwd.pool.o4;

import java.util.ArrayList;

public class ContactStore {

    ...

    public ContactInfo getByIndex(int i) {
        if (i>=0 && i < contactList.size()) {
            return contactList.get(i);
        }
        return null;
    }

    public void printNameAndIndex() {
        int i = 0;
        for (ContactInfo c : contactList) {
            System.out.println(i+": "+c.getName());
            i++;
        }
    }
    
    public static void main(String[] args) {
        ContactInfo c1 = new ContactInfo("Max", "27/12/2004", "01243 Uphill", "---");
        ContactInfo c2 = new ContactInfo("Sue", "17/02/2007", "01244 Downunder", "---");
        ContactStore s = new ContactStore();
        s.addContactInfo(c1);
        s.addContactInfo(c2);
        s.printNameAndIndex();
        ContactInfo ci = s.getByIndex(0);
        System.out.println(ci);
        ci = s.getByName("Max");
        System.out.println(ci);
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of an ArrayList collection class | completion task     | 1 - low |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of an ArrayList class

#### Learning Activities

1) read the given Java code
2) run the given program
3) implement the getByIndex-method
4) implement the printNameAndIndex-method
5) make use of the new implemented methods as part of the main-method
6) test and run the program

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5

[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0