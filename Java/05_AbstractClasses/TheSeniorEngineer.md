Topic: abstract classes

## Learning Task: The senior engineer

Read the given Java code of the class AbstractEmployee and Manager. Run the Manager class. 
Develop a new class of a SeniorEngineer inspired by the implementation of the Manager class. Ensure that the Senior Engineer's new salary will not grow more than 15% when it gets updated.

Demonstrate the SeniorEngineer class by an appropriate main-method implementation.

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

``` java
package org.htwd.pool.o5;

public class SeniorEngineer extends AbstractEmployee {

    public SeniorEngineer(String name, String department, int salary) {
        super(name, department, "Senior Engineer", salary);
    }

    @Override
    public boolean updateSalary(int salary) {
        if (salary<0 || salary > 1.15*this.getSalary())
            return false;
        return this.setSalary(salary);
    }

    public static void main(String[] args) {
        SeniorEngineer joe = new SeniorEngineer("Joe Blake", "Advanced Technologies", 70000);
        System.out.println(joe);
        boolean result = joe.updateSalary(80800);
        System.out.println(result);
        joe.setDepartment("Corporate Technologies");
        System.out.println(joe);
    }

}
``` 

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| practise the idea of abstract classes            | imitation task  | 1 - low        | 

#### Previous Knowledge

bcm-1: basics of classes, public/protected/private modifieres  
exi-1: basics of class extension  
abs-1: basics of abstract classes

#### Learning Activities

1) read the given Java code
2) run the code  
3) implement the SeniorEngineer class similar to the given Manager class
4) demonstrate the updateSalary feature in the implementation of the main-method

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 6  
[tutorialspoint.com: Java - Abstraction](https://www.tutorialspoint.com/java/java_abstraction.htm)  

Loy, M., Niemeyer, P. and Leuck, D. (2023). Learning Java (6th edition). O'Reilly Media, Inc.: 
Chapter 5, pages 172-174

---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2025            
License: CC BY-SA 4.0
