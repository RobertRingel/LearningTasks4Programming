package org.htwd.pool.o5;

public class BoxedBusinessCardPrinter extends AbstractBusinessCard {

    private int maxLineLength() {
        int maxLen = 0;
        for (String l : this.lines) {
            if (l.length()>maxLen)
                maxLen = l.length();
        }
        return maxLen;
    }

    private void printLine(int len) { 
        int i=0;
        while (i < len+2) {
            System.out.print('-'); i++;
        }
        System.out.println();
    }

    public static String getCenteredText(int width, String text) {
        int padding_l = (width - text.length()) / 2;
        int padding_r = padding_l;
        if (padding_l+text.length()+padding_r<width)
            padding_r++;
        String centeredText = String.format("%" + padding_l + "s%s%" + padding_r + "s", "", text, "");
        return centeredText;
    }

    @Override
    public void printCard() {
        int width = 4 + maxLineLength();
        printLine(width);

        for (String l : this.lines) {
            String text = "|" + BoxedBusinessCardPrinter.getCenteredText(width,l) + "|";
            System.out.println(text);
        }
        printLine(width);
    }

    public static void main(String[] args) {
        BoxedBusinessCardPrinter prt = new BoxedBusinessCardPrinter();
        prt.setLine(1,"Bob Miller");
        prt.setLine(2,"!the manager!");
        prt.setLine(3,"Tasteful Breweries Ltd.");
        prt.showLines();
        prt.printCard();
    }

}
