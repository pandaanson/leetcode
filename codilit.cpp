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
// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Summary of Problem:
// Given an array A consisting of N integers, the goal is to rotate the array K times.
// Rotation means each element is shifted right by one index, and the last element moves to the first place.
// Write a function that returns the rotated array A after K rotations.
// N and K are integers within the range [0..100].
// Each element of array A is an integer within the range [-1,000..1,000].


vector<int> solution(vector<int> &A, int K) {

    
    // Initialize an empty vector to store the rotated array
    vector<int> rotatedArray(A.size());
    
    // Get the size of the array for use in modulo operation and loop
    int N = A.size();
    
    // Edge case: Check if the array is empty or has only one element
    if (N <= 1) return A;

    // Perform rotation
    for (int i = 0; i < N; ++i) {
        // Calculate the new index after rotation
        int newIndex = (i + K) % N;
        
        // Assign the rotated value to the new index
        rotatedArray[newIndex] = A[i];
    }

    return rotatedArray;
}


int main() {
    vector<int> A1 = {3, 8, 9, 7, 6};
    vector<int> R1 = solution(A1, 3);
    for (auto& num : R1) {
        cout << num << " ";
    }
    cout << endl;

    vector<int> A2 = {0, 0, 0};
    vector<int> R2 = solution(A2, 1);
    for (auto& num : R2) {
        cout << num << " ";
    }
    cout << endl;

    vector<int> A3 = {1, 2, 3, 4};
    vector<int> R3 = solution(A3, 4);
    for (auto& num : R3) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
