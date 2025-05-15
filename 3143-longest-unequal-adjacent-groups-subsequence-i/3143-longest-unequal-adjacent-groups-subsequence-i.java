class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {

        Integer prev_ele = null;
        int n = words.length;
        List<String> res = new ArrayList<>();
        if (n==0) return res;

        for (int i=0; i<words.length; i++){
            if (prev_ele == null || groups[i] != prev_ele) {
                res.add(words[i]);
                prev_ele = groups[i];
            }
        }

        return res;
        
    }
}