class Solution {
    public boolean isValid(String s) {

        Deque<Character> stack = new ArrayDeque<>();
        HashMap<Character, Character> mapp = new HashMap<>();
        mapp.put('(', ')');
        mapp.put('[', ']');
        mapp.put('{', '}');

        for(Character ch: s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else if (ch == ')' || ch == ']' || ch == '}') {
                if (stack.isEmpty()) {
                    return false;
                }
                Character open = stack.pop();
                if (mapp.get(open) != ch) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
        
    }
}