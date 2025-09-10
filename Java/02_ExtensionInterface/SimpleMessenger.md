Topic: extension, interface

## Learning Task: The simple messenger

The code below shows the Messenger class that is a basic communication demo to send and receive text messages.

Read and run the code to obtain an understanding. Explain your understanding to another student.  
Define an interface class MessageXChange.java to define the send and receive methods and let the Messenger-class implement this interface.

``` java
package org.htwd.pool.o2;

public class Messenger {
    private String userName;
    private String lastMessage;
    private Messenger lastSender;

    public Messenger(String name) {
        this.userName = name;
        this.lastMessage = "";
        this.lastSender = null;
    }

    public boolean send(Messenger to, String msg) {
        return to.receive(this, msg);
    }

    public boolean receive(Messenger from, String msg) {
        if (from == null)
            return false;
        this.lastMessage = msg;
        this.lastSender = from;
        System.out.println("New msg from: "+from.getName());
        System.out.println(msg);
        return true;
    }

    public String getName() {
        return this.userName;
    }

    public String getLastMessage() {
        return this.lastMessage;
    }

    public static void main(String[] args) {
        Messenger a = new Messenger("Alex");
        Messenger b = new Messenger("Bianca");
        a.send(b,"Good morning! Meet for coffee?");
        if (b.getLastMessage().contains("coffee")) {
            b.send(a,"Great idea! See you in 3 minutes.");
        }
    }
}
```

---------------------------------------

### Solution

**The interface MessageXChange:**
``` java
package org.htwd.pool.o2;

public interface MessageXChange {
    public boolean send(Messenger to, String msg);
    public boolean receive(Messenger from, String msg);
}
```

**The Messenger implementing the interface:**
``` java
package org.htwd.pool.o2;

public class Messenger implements MessageXChange {
    ...
}

```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| definition of an interface out of a Java class implementation | completion task | 1 - low        |

#### Previous Knowledge

bcm-1: basics of classes, public/private/final modifieres  
exi-2: basics of interface definition and implementation 

#### Learning Activities

1) read and run the given Java code
2) explain the understanding to another student
3) implement the requested interface definition
4) let the given class implement the defined interface 

#### Supporting information

[Java-OOP-Poster](../JavaPosterOOP_engl.pdf): Box 4

[tutorialspoint.com: Java - Interfaces](https://www.tutorialspoint.com/java/java_interfaces.htm)  

ToDo: Matthes, E. (2019). Python crash course a hands-on, project-based introduction to programming (2nd edition). No Starch Press.:  
Chapter 2, pages 15-32, Chapter 7, pages 114-116  


---------------------------------------
Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 09/2025            
License: CC BY-SA 4.0
