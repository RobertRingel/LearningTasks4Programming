package org.htwd.pool.o2;

public class Book {
    private final String title;
    private final String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    public String getTitle() { return this.title; }
    public String getAuthor() { return this.author; }

    public String toString() {
        StringBuilder sb = new StringBuilder(this.author);
        sb.append(" : ");
        sb.append(this.title);
        return sb.toString();
    }
}
