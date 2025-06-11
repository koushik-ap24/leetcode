class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = a & b; // Calculate new carry bits
            a = a ^ b; // sum with carry
            b = carry << 1; // Shift carry to the left
        }
        return a; // Final result
    }
}