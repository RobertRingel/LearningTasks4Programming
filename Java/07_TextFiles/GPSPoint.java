package org.htwd.pool.o7;

public class GPSPoint {
    private double lon;
    private double lat;

    public GPSPoint(double lat, double lon) {
        this.lat = lat;
        this.lon = lon;
    }

    public double getLatitude() {
        return this.lat;
    }

    public double getLongitude() {
        return this.lon;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder("Lat:");
        sb.append(this.lat);
        sb.append(" : Lon:");
        sb.append(this.lon);
        return sb.toString();
    }
}
