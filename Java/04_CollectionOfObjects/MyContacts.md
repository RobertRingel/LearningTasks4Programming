Topic: storing objects in collections

## Learning Task: My Contacts

Given is the code of the two Java classes ContactInfo and ContactStore, whereas ContactInfo is an extension of the already known class [Person](../03_UsingObjects/Person.java).

Read the given code and discuss it with another student before you write a brief explanation of it.
Proof your understanding by implementing an appropriate main-method to show the usage of the class ContactStore.

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

}
```

---------------------------------------

### Solution

The class ContactInfo is an extension of the class Person. It is used to store basic information about individual contacts to other person in related class attributes. Byside the Person class attributes name and birthday the string attributes address and mobile phone number are part of this class. The class uses the constructor to store these attributes and it provides two get-methods to provide address and mobile number.

The class ContactStore uses an ArrayList to store ContactInfo objects in a list like fashion. The addContactInfo-method is available to add data to the store. To obtain data from the store one can use the getByName-method. In case the given name yields a contact in the store the related ContactInfo-object will be returned - otherwise null will be returned. The removeByName-method can be used to delete a contact from the store. The object will be looked up by the given name of a person. In case of successful removal the method will return true.

The implementation of the below main-method demonstrates these features of the class.  

``` java
package org.htwd.pool.o4;

import java.util.ArrayList;

public class ContactStore {

    ...

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

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the use of an ArrayList collection class | worked-out-example  | 1 - low |  

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of an ArrayList class

#### Learning Activities

1) read the given Java code
2) discuss the the code with another student
3) write a brief explanation of the two given Java classes
4) implement a main method in class ContactStore to demonstrate the class usage
5) test and run the program

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5

[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0
