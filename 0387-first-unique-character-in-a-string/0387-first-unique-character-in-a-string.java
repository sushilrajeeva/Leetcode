class Solution {
    public int firstUniqChar(String s) {

        int [] cache = new int[26];

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            cache[getIndexValue(ch)] += 1;
        }

        for (int i = 0; i < s.length(); i++) {
            int index = getIndexValue(s.charAt(i));
            if (cache[index] == 1) return i;
        }
        return -1;
        
    }

    public int getIndexValue(char ch) {
        return (int)(ch - 'a');
    }
}