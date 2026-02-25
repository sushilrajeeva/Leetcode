class Solution {
    public boolean isAnagram(String s, String t) {

        int l1 = s.length();
        int l2 = t.length();

        if (l1 != l2) return false;

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i<l1; i++) {
            Character k1 = s.charAt(i);
            Character k2 = t.charAt(i);

            sMap.put(k1, sMap.getOrDefault(k1, 0) + 1);
            tMap.put(k2, tMap.getOrDefault(k2, 0) + 1);
        }

        int s_len = sMap.size();
        int t_len = tMap.size();

        if (s_len != t_len) return false;

        return sMap.equals(tMap);
        
    }
}