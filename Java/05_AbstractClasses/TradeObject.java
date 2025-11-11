package org.htwd.pool.o5;

public class TradeObject {

    private String itemName;
    private double price;
    private String sellerID;
    private String buyerID;

    public TradeObject(String item, double price, String sellerID) {
        this.itemName = item;
        this.sellerID = sellerID;
        this.buyerID = "";
        this.price = price;
    }

    public double getPrice() {
        return this.price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public void setBuyer(String buyerID) {
        this.buyerID = buyerID;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.itemName);
        sb.append(" : EUR:");
        sb.append(this.price);
        sb.append(" : Seller:");
        sb.append(this.sellerID);
        sb.append(" : Buyer:");
        sb.append(this.buyerID);
        return sb.toString();
    }
}
