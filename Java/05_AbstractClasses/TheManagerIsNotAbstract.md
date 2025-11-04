Topic: abstract classes

## Learning Task: The manager is not abstract

Read the given Java code of the class AbstractEmployee and Manager. Run the Manager class. Talk about the given code with another student inorder to obtain an understanding.

Express your understaning in a written a brief description of the two classes.

**The basic class of an employee**

``` java
package org.htwd.pool.o5;

abstract public class AbstractEmployee {
    private String name;
    private String department;
    private String job;
    private int salary;

    public AbstractEmployee(String name, String department, String job, int salary) {
        this.name = name;
        this.department = department;
        this.job = job;
        this.salary = salary;
    }

    public String getName() { return this.name; }
    public String getDepartment() { return this.department; }
    public String getJob() { return this.job; }
    public int getSalary() { return this.salary; }

    protected boolean setSalary(int salary) {
        if (salary<0)
            return false;
        this.salary = salary;
        return true;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public void setJob(String job) {
        this.job = job;
    }

    abstract public boolean updateSalary(int salary);

    public String toString() {
        StringBuilder sb = new StringBuilder(this.name);
        sb.append(" : ");
        sb.append(this.job);
        sb.append(" : ");
        sb.append(this.department);
        sb.append(" : EUR:");
        sb.append(this.salary);
        return sb.toString();
    }
}
``` 

**The class of a manager**
``` java
package org.htwd.pool.o5;

public class Manager extends AbstractEmployee {

    public Manager(String name, String department, int salary) {
        super(name, department, "Manager", salary);
    }

    public void setJob(String job) {
        if (job.toLowerCase().contains("manager"))
            super.setJob(job);
    }

    @Override
    public boolean updateSalary(int salary) {
        if (salary<0 || salary < this.getSalary())
            return false;
        return this.setSalary(salary);
    }

    public void printCard() {
        System.out.println("--- Business Card ---");
        String data = this.toString();
        data = data.replaceAll(" : ", "\n");
        int i = data.indexOf("EUR:");
        String text = data.substring(0,i);
        System.out.println(text);
    }

    public static void main(String[] args) {
     Manager sue = new Manager("Sue Miller", "Advanced Technologies", 70000);
     System.out.println(sue);
     sue.updateSalary(75000);
     sue.setDepartment("Corporate Technologies");
     System.out.println(sue);
     sue.printCard();
    }

}
``` 

---------------------------------------

### Solution

The class AbstractEmployee provides the basic functionality of an employee object by implementing primary attributes, the related getter-, setter-methods and a toString-method. The updateSalary-method however is abstract. So it is not possible to create objects of the class AbstractEmployee - the class is labelled "abstract". Any sub-class of this class needs to implement the updateSalary-method. This can be used to implement necessary safety checks when changing an employee's salary.  
The class Manager is a sub-class of AbstractEmployee. It implements the updateSalary-method including a manager-related-safety check!  Furthermore the Manager-class re-implements the setJob-Method in a way, to ensure a Manager-relqated job title. Last but not least the Manager class provides a method to print a business card. The main-method demonstrates some key features of this class.

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| understand the idea of abstract methods and classes | worked-out example | 1 - low  | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension 
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code
2) run the code  
3) discuss the code with another student
4) write a brief description of the given code

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
