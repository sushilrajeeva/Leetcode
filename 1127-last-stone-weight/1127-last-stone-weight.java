import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public int lastStoneWeight(int[] stones) {

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for(int stone : stones) {
            maxHeap.offer(stone);
        }

        while(maxHeap.size() > 1) {
            int stone1 = maxHeap.poll();
            int stone2 = maxHeap.poll();

            int newStone = stone1 - stone2;
            
            if(newStone > 0) {
                maxHeap.offer(newStone);
            }
        }

        return maxHeap.size() == 0 ? 0 : maxHeap.peek();
        
    }
}