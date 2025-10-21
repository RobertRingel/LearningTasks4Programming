package org.htwd.pool.o4;

public class StockItem {
    private String stockCode;
    private double pieces;
    private double price;

    public StockItem(String code, double pcs, double price) {
        this.stockCode = code;
        this.pieces = pcs;
        this.price = price;
    }

    public boolean updatePrice(double price) {
        if (price > 0.0) {
            this.price = price;
            return true;
        }
        return false;
    }

    public String getStockCode() {return this.stockCode; }
    public double getPrice() {return this.price; }
    public double getPieces() {return this.pieces; }

    public String toString() {
        StringBuilder sb = new StringBuilder("StockItem: ");
        sb.append(this.getStockCode());
        sb.append(" : Price: ");
        sb.append(this.getPrice());
        sb.append(" : Pieces: ");
        sb.append(this.getPieces());
        return sb.toString();
    }

    public static void main(String[] args) {
        StockItem si = new StockItem("IBM", 4.0, 32.54);
        System.out.println(si);
        si.updatePrice(33.02);
        System.out.println(si);
    }
}
