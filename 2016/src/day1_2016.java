//--- Day 1: No Time for a Taxicab ---
//        Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.
//
//        Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
//
//        You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
//
//        The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.
//
//        There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
//
//        For example:
//
//        Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
//        R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
//        R5, L5, R5, R3 leaves you 12 blocks away.
//        How many blocks away is Easter Bunny HQ?

import java.io.FileNotFoundException;
import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.List;

public class day1_2016 {
    static String curr_dir = "up";
    static int[] pos = {0, 0};
    static ArrayList<List<Integer>> visited_locations = new ArrayList<>(1);
    static ArrayList<Character> rotations = new ArrayList<Character>();
    static ArrayList<Integer> distances = new ArrayList<Integer>();

    private static void rotate(Character rotation) {
        if (curr_dir.equals("up")) {
            if (rotation == 'R') {
                curr_dir = "right";
            }
            else {
                curr_dir = "left";
            }
        }
        else if (curr_dir.equals("down")) {
            if (rotation == 'R') {
                curr_dir = "left";
            }
            else {
                curr_dir = "right";
            }
        }
        else if (curr_dir.equals("left")) {
            if (rotation == 'R') {
                curr_dir = "up";
            }
            else {
                curr_dir = "down";
            }
        }
        else if (curr_dir.equals("right")) {
            if (rotation == 'R') {
                curr_dir = "down";
            }
            else {
                curr_dir = "up";
            }
        }
    }

    private static void move(int distance) {
        for (int i = 0; i < distance; i++) {
            if (curr_dir.equals("up")) {
                pos[1]++;
            }
            else if (curr_dir.equals("down")) {
                pos[1]--;
            }
            else if (curr_dir.equals("left")) {
                pos[0]++;
            }
            else if (curr_dir.equals("right")) {
                pos[0]--;
            }
        }
    }

    public static void main(String[] args) {
        // Start at 0,0.
        visited_locations.add(Arrays.asList(0,0));
        //static int[] first_visited_twice = new int[]();
        try {
            File input = new File("./day1_2016_input.txt");
            Scanner scanner = new Scanner(input);

            while (scanner.hasNext()) {
                String thisline = scanner.next();
                rotations.add(thisline.charAt(0));
                if (thisline.length() >= 2) {
                    if (thisline.charAt(thisline.length() - 1) == ',') {
                        distances.add(Integer.parseInt(thisline.substring(1, thisline.length() - 1)));
                    } else {
                        distances.add(Integer.parseInt(thisline.substring(1, thisline.length())));
                    }
                }
            }
        }
        catch (FileNotFoundException e) {
            System.out.println("The input text file was not found.");
        }

        for (int i = 0; i < rotations.size(); i++) {
            rotate(rotations[i]);
            move(distances[i]);
        }
    }
}

