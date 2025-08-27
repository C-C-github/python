import java.util.*;

public class Solution {
    public int minMoves(int sx, int sy, int tx, int ty) {
        if (sx > tx || sy > ty) return -1; // Cannot reach if start exceeds target
        
        Queue<long[]> queue = new ArrayDeque<>();
        Set<Long> visited = new HashSet<>();
        
        queue.offer(new long[]{tx, ty, 0});
        visited.add(encode(tx, ty));
        
        while (!queue.isEmpty()) {
            long[] current = queue.poll();
            int x = (int) current[0], y = (int) current[1],
             steps = (int) current[2];
            
            if (x == sx && y == sy) return steps;
            if (x < sx || y < sy) continue; // Prune if below start
            
            int m = Math.max(x, y);
            
            // Try subtracting m from x
            if (x - m >= sx) {
                long nx = x - m, ny = y;
                long key = encode((int) nx, (int) ny);
                if (!visited.contains(key)) {
                    visited.add(key);
                    queue.offer(new long[]{nx, ny, steps + 1});
                }
            }
            
            // Try subtracting m from y
            if (y - m >= sy) {
                long nx = x, ny = y - m;
                long key = encode((int) nx, (int) ny);
                if (!visited.contains(key)) {
                    visited.add(key);
                    queue.offer(new long[]{nx, ny, steps + 1});
                }
            }
        }
        
        return -1;
    }
    
    private long encode(int x, int y) {
        return ((long) x << 32) | (y & 0xffffffffL);
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minMoves(1, 2, 5, 4)); // Output: 2
        System.out.println(sol.minMoves(0, 1, 2, 3)); // Output: 3
        System.out.println(sol.minMoves(1, 1, 2, 2)); // Output: -1
    }
}