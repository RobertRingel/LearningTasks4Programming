Topic: abstract classes

## Learning Task: The abstract student

Read the given Java code of the class AbstractStudent. 
Develop a new class of a non-abstract Student based on the given class. First implement a minimum version of the new Student class that can be used to create student objects. Add a main-method to the class to demonstrate the creation of student objects.  
Finally feel free to add some additional functionality of your choice to the new student class.  

***Note:*** the AbstractStudent is an extension of the class [Person](../03_UsingObjects/Person.java) from this task repository.

``` java
package org.htwd.pool.o5;

import org.htwd.pool.o3.Person;
import java.util.ArrayList;

public abstract class AbstractStudent extends Person {

    private final String studentID;
    private final String DELIMITER = ":";
    protected ArrayList<String> gradings = new ArrayList<String>();

    public AbstractStudent(String name, String bday, String studentID) {
        super(name, bday);
        this.studentID = studentID;
    }

    public String getStudentID() {return this.studentID; }

    public void recordGradingMark(String lecture, String mark, int credits) {
        String gradingMark = lecture + DELIMITER + mark + DELIMITER + Integer.toString(credits);
        gradings.add(gradingMark);
    }

    public void printFilteredGradingMarks(String filter) {
        if (filter=="")
            filter = DELIMITER;
        for (String gm : gradings) {
            if (gm.indexOf(filter) >= 0)
                System.out.println(gm);
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(super.toString());
        sb.append(" StudentID:");
        sb.append(getStudentID());
        return sb.toString();
    }
}
``` 

---------------------------------------

### Solution

**Minimalistic solution**

``` java
package org.htwd.pool.o5;

public class Student extends AbstractStudent {

    public Student(String name, String bday, String studentID) {
        super(name, bday, studentID);
    }

    public String toString() {
        return super.toString();
    }

    public static void main(String[] args) {
        Student bob = new Student("Bob McAllister", "15/09/2009", "57-123-9987");
        bob.recordGradingMark("Basic Statistics","3.7", 3);
        bob.recordGradingMark("AI for beginners", "1.3", 4);
        System.out.println(bob);
        bob.printFilteredGradingMarks("");
        System.out.println("--------------");
        bob.printFilteredGradingMarks("AI");
    }
}
``` 

**Solution including some code extension**

``` java
package org.htwd.pool.o5;

public class Student extends AbstractStudent {

    private String degreeProgram = "";

    public Student(String name, String bday, String studentID) {
        super(name, bday, studentID);
    }

    public boolean enrollToDegreeProgram(String progr) {
        if (this.degreeProgram == "") {
            this.degreeProgram = progr;
            return true;
        }
        return false;
    }

    private String getDegreeProgram() { return this.degreeProgram; }

    public String toString() {
        StringBuilder sb = new StringBuilder(super.toString());
        sb.append(" : Degree Program: ");
        sb.append(getDegreeProgram());
        return sb.toString();
    }

    public static void main(String[] args) {
        Student bob = new Student("Bob McAllister", "15/09/2009", "57-123-9987");
        bob.enrollToDegreeProgram("Global Economics");
        bob.recordGradingMark("Basic Statistics","3.7", 3);
        bob.recordGradingMark("AI for beginners", "1.3", 4);
        System.out.println(bob);
        bob.printFilteredGradingMarks("");
        System.out.println("--------------");
        bob.printFilteredGradingMarks("AI");
    }
}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the idea of abstract classes          | non-specific goal task  | 2 - nomal | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
col-1: basics of ArrayLists  
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code
2) implement and test the minimalistic solution    
3) add some new code to the minimalistic solution  
4) test the new class implementation

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 172-174 

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
