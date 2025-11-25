package org.htwd.pool.o7;

import org.htwd.pool.o2.GPSPoint;

import java.io.*;
import java.util.ArrayList;

public class GPSTrack {
    private ArrayList<GPSPoint> track = new ArrayList<GPSPoint>();
    private final String DELIMITER = ";";

    public GPSTrack() { }

    public void loadFromFile(String filename) {
        String line;
        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            while ((line = br.readLine()) != null) {
                String[] token = line.split(DELIMITER);
                if (token.length != 2)
                    throw new RuntimeException("corrupt line:"+line);
                double lat = Double.parseDouble(token[0].strip());
                double lon = Double.parseDouble(token[1].strip());
                this.addPoint(lat, lon);
            }
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found:"+filename);
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (RuntimeException e) {
            System.out.println("Error while reading a file:"+e.getMessage());
        }
    }

    public void writeToFile(String filename) {
        try {
            FileWriter writer = new FileWriter(filename, false);
            for (GPSPoint p : this.track) {
                double lat = p.getLatitude();
                double lon = p.getLongitude();
                String line = lat+DELIMITER+lon+"\n";
                writer.write(line);
            }
            writer.close();
        } catch(IOException e) {
            System.out.println("Error writing track file: "+e.getMessage());
        }
    }

    public void addPoint(double lat, double lon) {
        GPSPoint p = new GPSPoint(lat, lon);
        track.add(p);
    }

    public boolean removePoint(int i) {
        if (i<0 || i> track.size())
            return false;
        track.remove(i);
        return true;
    }

    public GPSPoint getPoint(int i) {
        if (i<0 || i> track.size())
            return null;
        return track.get(i);
    }

    public int size() {
        return track.size();
    }

    public static void main(String[] args) {
        GPSTrack t = new GPSTrack();
        t.loadFromFile("track01.txt");
        /*
        t.addPoint(52.123, 12.01);
        t.addPoint(52.124, 12.00);
        t.addPoint(52.125, 12.01);
        t.addPoint(52.126, 12.03);   */
        int n = t.size();
        int i = 0;
        while (i<n) {
            GPSPoint p = t.getPoint(i);
            i++;
            System.out.println(p);
        }
        //t.writeToFile("track01.txt");
        t.removePoint(1);
        System.out.println(t.size());
    }

}
