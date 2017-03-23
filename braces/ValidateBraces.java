import java.util.Stack;
import java.util.HashMap;

public class ValidateBraces {
    
    public static void main(String args[]) {
        
        String [] tests = {
            "{}[({})]",
            "{}[{()]",
            "{[}]({})}",
            "{()[]]]}",
            "()",
            "(){}[][{()}]",
            "[[[[]]])"
        };
        
        for (int i = 0; i < tests.length; i++) {
            System.out.println(validateBraces(tests[i])); 
        }
    }

    public static boolean validateBraces(String bracesString) {
        
        if (bracesString.length() % 2 != 0) {
            return false;
        }
        
        HashMap<Character,Character> map = new HashMap();
        map.put('[', ']');
        map.put('(', ')');
        map.put('{', '}');
        
        Stack stack = new Stack();
        char[] bracesCharArr = bracesString.toCharArray();
        for (int i = 0; i < bracesString.length(); i++) {
            if (bracesCharArr[i] == '(' || 
                bracesCharArr[i] == '{' || 
                bracesCharArr[i] == '[') {
                stack.push(bracesCharArr[i]);
            } else if ((Character) bracesCharArr[i] == map.get((Character)stack.peek())) {
                stack.pop();
            } else {
                return false;
            }
        }
        return true;
    }
}
