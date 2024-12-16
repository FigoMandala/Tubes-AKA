import time

def kmp_pattern_search(text, pattern):
    # Preprocess the pattern to create the longest prefix suffix (LPS) array
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    start_time = time.time()
    kmp_pattern_search(text, pattern)
    end_time = time.time()

    execution_time_ms = (end_time - start_time) * 1000  
    print(f"Execution time: {execution_time_ms:.10f} ms")
