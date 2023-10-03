#include <iostream>
#include <algorithm>
using namespace std;

// Summary of Problem:
// Given a positive integer N, find the longest sequence of consecutive zeros
// that are surrounded by ones at both ends in its binary representation.
// Return the length of the longest such sequence, or 0 if there isn't one.
// N is within the range [1, 2,147,483,647].

int solution(int N) {
    // Initialize a variable to store the length of the longest binary gap
    int longest_gap = 0;
    
    // Initialize a variable to store the length of the current binary gap
    int current_gap = 0;
    
    // Initialize a flag to check if we've encountered a '1' in the binary representation
    bool found_one = false;
    
    // Loop through each bit in the binary representation of N
    while (N > 0) {
        // If the last bit is 1
        if (N & 1) {
            // Update the longest binary gap if the current gap is greater
            longest_gap = max(longest_gap, current_gap);
            
            // Reset the current gap length
            current_gap = 0;
            
            // Set the flag to indicate we've found a '1'
            found_one = true;
        }
        // If the last bit is 0 and we have found at least one '1'
        else if (found_one) {
            // Increment the current gap length
            current_gap++;
        }
        
        // Right-shift N to check the next bit
        N >>= 1;
    }
    
    return longest_gap;
}

int main() {
    cout << solution(1041) << endl; // Should return 5
    cout << solution(32) << endl;   // Should return 0
    return 0;
}
