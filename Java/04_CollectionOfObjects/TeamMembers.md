Topic: storing objects in collections

## Learning Task: Team Members

Given is the following Java class FamilyMembers. Read and run the code to obtain an understanding.  

Use this class as a blueprint to design and implement a class TeamMembers to store objects of class [Employee](../03_UsingObjects/Employee.java).  
Test your implementation with help of an appropriate main-method.

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

``` java
package org.htwd.pool.o4;

import org.htwd.pool.o3.Account;
import org.htwd.pool.o3.Employee;
import org.htwd.pool.o3.Person;

import java.util.ArrayList;
import java.util.HashMap;

public class TeamMembers {

    private HashMap<String, Employee> members = new HashMap<String, Employee>();

    public TeamMembers() {}

    public void addPerson(String role, Employee p) {
        members.put(role, p);
    }

    public Employee getPerson(String role) {
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
        Person sue = new Person("Sue", "21/02/2001");
        Account acc_sue = new Account("DE786354322134", sue);
        Employee eSue = new Employee(sue, acc_sue);

        Person bob = new Person("Bob", "27/12/2002");
        Account acc_bob = new Account("DE123454322134", bob);

        Employee eBob = new Employee(bob, acc_bob);
        TeamMembers team = new TeamMembers();
        team.addPerson("Manager", eSue);
        team.addPerson("DeputyMgr.", eBob);
        ArrayList<String> roles = team.getAllRoles();
        for (String r:roles) {
            Employee p = team.getPerson(r);
            System.out.println(p);
        }

        team.removePerson("Manager");
        System.out.println(team.getPerson("DeputyMgr."));
    }

}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the use of the HashMap and ArrayList collection classes | imitation task | 2 - normal | 

#### Previous Knowledge

bcm-1: basics of classes, public/private modifieres  
uob-1: basics of creating and using objects  
col-1: basics of the HashMap and ArrayList classes

#### Learning Activities

1) read the given Java code
2) run the program
3) design and implement the TeamMembers-class
4) run and test the new implemented class

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 5  
[tutorialspoint.com: Java - HashMap](https://www.tutorialspoint.com/java/util/java_util_hashmap.htm)  
[tutorialspoint.com: Java - ArrayList](https://www.tutorialspoint.com/java/util/java_util_arraylist.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2025            
License: CC BY-SA 4.0
