class Solution {
    public int[][] highFive(int[][] items) {

        Map<Integer, PriorityQueue<Integer>> topScores = new HashMap<>();
        PriorityQueue<Integer> ids = new PriorityQueue<>();

        for (int[] item : items) {
            int studentId = item[0];
            int score = item[1];

            if (!topScores.containsKey(studentId)) {
                topScores.put(studentId, new PriorityQueue<>());
                ids.add(studentId);
            }
            topScores.get(studentId).add(score);
            if (topScores.get(studentId).size() > 5) {
                topScores.get(studentId).poll();
            }
        }

        List<List<Integer>> result = new ArrayList<>();

        while (ids.size() > 0) {
            int id = ids.poll();
            int totalScore = 0;
            PriorityQueue<Integer> pq = topScores.get(id);
            for (int score : pq) {
                totalScore += score;
            }
            int avg = (totalScore)/pq.size();

            result.add(new ArrayList<>(Arrays.asList(id, avg)));

        }

        int m = result.size();
        int[][] output = new int[m][2];

        for (int i = 0; i < m; i++) {
            output[i][0] = result.get(i).get(0);
            output[i][1] = result.get(i).get(1);
        }

        return output;
    }
}