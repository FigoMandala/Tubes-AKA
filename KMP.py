import time

class KMPMatcher:
    def __init__(self):
        self.comparisons = 0
        self.execution_time = 0
        
    def compute_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m  
        
        length = 0 
        i = 1       
        
        while i < m:
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
    
    def search(self, text, pattern):
        if not text or not pattern:
            return [], 0, 0
            
        self.comparisons = 0
        matches = []
        
        start_time = time.time()
        
        n = len(text)
        m = len(pattern)
        
        lps = self.compute_lps(pattern)
        
        i = 0  
        j = 0 
        
        while i < n:
            self.comparisons += 1
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
            
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                    
        self.execution_time = (time.time() - start_time) * 1000
        
        return matches, self.comparisons, self.execution_time
    
    def print_results(self, text, pattern, matches):
        print("\nHasil Pencarian KMP Pattern Matching:")
        print("-" * 50)
        print(f"Pattern: {pattern}")
        print(f"Jumlah kecocokan ditemukan: {len(matches)}")
        print(f"Posisi kecocokan: {matches}")
        print(f"Jumlah perbandingan: {self.comparisons}")
        print(f"Waktu eksekusi: {self.execution_time:.4f} ms")
        

def main():
    matcher = KMPMatcher()
    
    text = ""
    pattern = ""
    
    matches, comparisons, execution_time = matcher.search(text, pattern)
    
    matcher.print_results(text, pattern, matches)

if __name__ == "__main__":
    main()
