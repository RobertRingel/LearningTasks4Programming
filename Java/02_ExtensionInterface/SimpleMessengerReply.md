Topic: extension, interface

## Learning Task: The simple messenger reply service

The code below shows the Messenger class that is a basic communication demo to send and receive text messages. It also provides the code of the interface class MessageXChange.

Read and run the code to obtain an understanding. Explain your understanding to another student.  

Extend the implementation towards a reply-method that should become part of the interface definition: boolean reply(String msg)  
The reply method shlould send the given message to the sender of the message received right before.  
Test your implementation using the main-method-code.

**The interface MessageXChange:**
``` java
package org.htwd.pool.o2;

public interface MessageXChange {
    public boolean send(Messenger to, String msg);
    public boolean receive(Messenger from, String msg);
}
```

**The Messenger class**
``` java
package org.htwd.pool.o2;

public class Messenger implements MessageXChange {
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
        if (b.getLastMessage().contains("coffee")) 
            b.send(a,"Great idea! See you in 3 minutes.");
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
    public boolean reply(String msg);
}
```

**The Messenger implementing the interface:**
``` java
package org.htwd.pool.o2;

public class Messenger implements MessageXChange {
    ...

    public boolean reply(String msg) {
        if (this.lastSender != null)
            return send(this.lastSender, msg);
        return false;
    }

    public static void main(String[] args) {
        Messenger a = new Messenger("Alex");
        Messenger b = new Messenger("Bianca");
        a.send(b,"Good morning! Meet for coffee?");
        if (b.getLastMessage().contains("coffee")) 
            b.reply("Great idea! See you in 3 minutes.");
    }
}
```

| **Learning objective**                           | **Task type**   | **Complexity** |
| ------------------------------------------------ | --------------- | -------------- |
| definition and implementation of an interface     | completion task | 1 - low        |

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
