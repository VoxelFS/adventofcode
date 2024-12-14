import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

class Day2 {
    public static void main(String[] args) {
        File file = new File("inputs/day2.txt");
        int safe = 0;
        int safe2 = 0;
        try {
            Scanner myReader = new Scanner(file);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] splited = data.split("\\s+");
                Integer[] intArr = new Integer[splited.length - 1];
                for (int i = 1; i < splited.length; i ++) {
                    int prev = Integer.parseInt(splited[i-1]);
                    int curr = Integer.parseInt(splited[i]);
                    int diff = curr - prev;
                    intArr[i-1] = diff;
                }
                if (safetyCheck(intArr) && safetyCheck2(intArr)) {
                    safe++;
                }
                if (safetyCheck3(splited)) {
                    safe2++;
                }
                
            }
            myReader.close();
            System.out.println(safe);
            System.out.println(safe2);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
    }

    static boolean safetyCheck(Integer[] arr) {
        int sign = Integer.compare(arr[0], 0);

        for (int num : arr) {
            if (Integer.compare(num, 0) != 0 && Integer.compare(num, 0) != sign) {
                return false;
            }
        }

        return true;
    }

    static boolean safetyCheck2(Integer[] arr) {
        Integer[] check = {1, 2, 3};
        for (int s : arr) {
            if (!Arrays.asList(check).contains(Math.abs(s))) {
                return false;
            }
        }
        return true;
    }

    static boolean safetyCheck3(String[] arr) {
        for (int i = 0; i < arr.length; i++) {
            Integer[] modifiedArr = new Integer[arr.length - 1];
            int idx = 0;
            for (int j = 0; j < arr.length; j++) {
                if (j != i) {
                    modifiedArr[idx++] = Integer.parseInt(arr[j]);
                }
            }
            Integer[] intArr = new Integer[modifiedArr.length - 1];
                for (int k = 1; k < modifiedArr.length; k ++) {
                    int prev = modifiedArr[k-1];
                    int curr = modifiedArr[k];
                    int diff = curr - prev;
                    intArr[k-1] = diff;
            }
            if (safetyCheck(intArr) && safetyCheck2(intArr)) {
                return true;
            }
        
        }
        return false;
    }
}