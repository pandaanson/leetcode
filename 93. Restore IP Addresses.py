class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(current_string, string_left, current_chunk):
            # Base case: if the last chunk is reached
            if current_chunk == 4:
                # Check if there's no string left and add the current string to the answer
                if not string_left:
                    ans.append(current_string[:-1])  # Remove the trailing dot
                return

            # Recursively build the IP address for the first three chunks
            for i in range(1, 4):
                if i <= len(string_left):
                    chunk = string_left[:i]
                    # Check for leading zeros and valid integer range
                    if (chunk == "0" or not chunk.startswith("0")) and 0 <= int(chunk) <= 255:
                        dfs(current_string + chunk + ".", string_left[i:], current_chunk + 1)

        ans = []
        dfs("", s, 0)
        return ans
