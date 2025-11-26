package org.htwd.pool.o7;

import java.util.ArrayList;

public abstract class AbstractBusinessCard {    
    protected ArrayList<String> lines = new ArrayList<String>();

    public AbstractBusinessCard() {
        int i=0;
        while (i<8) {
            lines.add("");
            i++;
        }
    }

    public boolean setLine(int line, String text) {
        if ((line<1) || (line>8))
            return false;
        lines.set(line, text);
        return true;
    }

    public void showLines() {
        for (String l : lines)
            System.out.println(l);
    }

    abstract public void printCard();   
}
