import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CardConverter {


    public static void main(String[] args) throws IOException {


        String a = "\uD83C\uDCA1";
        String[] spades = {"\uD83C\uDCA1", "\uD83C\uDCA2", "\uD83C\uDCA3", "\uD83C\uDCA4", "\uD83C\uDCA5", "\uD83C\uDCA6", "\uD83C\uDCA7", "\uD83C\uDCA8", "\uD83C\uDCA9", "\uD83C\uDCAA", "\uD83C\uDCAB", "\uD83C\uDCAD", "\uD83C\uDCAE"};
        String[] hearts = {"\uD83C\uDCB1", "\uD83C\uDCB2", "\uD83C\uDCB3", "\uD83C\uDCB4", "\uD83C\uDCB5", "\uD83C\uDCB6", "\uD83C\uDCB7", "\uD83C\uDCB8", "\uD83C\uDCB9", "\uD83C\uDCBA", "\uD83C\uDCBB", "\uD83C\uDCBD", "\uD83C\uDCBE"};
        String[] diamonds = {"\uD83C\uDCC1", "\uD83C\uDCC2", "\uD83C\uDCC3", "\uD83C\uDCC4", "\uD83C\uDCC5", "\uD83C\uDCC6", "\uD83C\uDCC7", "\uD83C\uDCC8", "\uD83C\uDCC9", "\uD83C\uDCCA", "\uD83C\uDCCB", "\uD83C\uDCCD", "\uD83C\uDCCE"};
        String[] clubs = {"\uD83C\uDCD1", "\uD83C\uDCD2", "\uD83C\uDCD3", "\uD83C\uDCD4", "\uD83C\uDCD5", "\uD83C\uDCD6", "\uD83C\uDCD7", "\uD83C\uDCD8", "\uD83C\uDCD9", "\uD83C\uDCDA", "\uD83C\uDCDB", "\uD83C\uDCDD", "\uD83C\uDCDE"};
        List<String[]> suits = new ArrayList<>(Arrays.asList(spades, hearts, diamonds, clubs));


        InputStreamReader ir = new InputStreamReader(new FileInputStream(new File(args[0])));
        int c;
        boolean start = false;
        StringBuilder sb = new StringBuilder();
        while ((c = ir.read()) != -1) {
            if (c == '[') start = true;
            if (start) {
                sb.append((char) c);
            }
        }

        String[] array = sb.toString().replaceAll("(\\[|\\]|\\s*)", "").split(",");
        int n = (int) Math.sqrt(array.length);
        String[][] moves = new String[n][n];
        int counter = 0;
        for (String[] row : moves) {
            for (int i = 0; i < row.length; i++) {
                int value = Integer.parseInt(array[counter]);
                if (value == -1) {
                    row[i] = "";
                } else {
                    String[] card_suit = suits.get(Math.floorDiv(value, 13));
                    String card = card_suit[Math.floorMod(value, 13)];
                    row[i] = card;
                }
                counter++;
            }
        }

        for (String[] move : moves) {
            for (String s : move) {
                if(!s.isEmpty()) {
                    System.out.print(s+ "  ");
                }
            }
            System.out.print("\n");


        }


    }

}
