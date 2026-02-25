class Solution {
    public boolean isAnagram(String s, String t) {

        int l1 = s.length();
        int l2 = t.length();

        if (l1 != l2) return false;

        Map<Character, Integer> mapp = new HashMap<>();

        for (int i = 0; i<l1; i++) {
            Character k1 = s.charAt(i);

            mapp.put(k1, mapp.getOrDefault(k1, 0) + 1);
        }

        for (int i = 0; i<l2; i++) {
            Character k2 = t.charAt(i);
            if (!mapp.containsKey(k2)) return false;

            mapp.put(k2, mapp.get(k2) - 1);

        }

        for (Map.Entry<Character, Integer> entry: mapp.entrySet()) {
            if (entry.getValue() != 0) return false;
        }

        return true;
        
    }
}