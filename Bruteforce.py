import time

class BruteForceStringMatcher:
    def __init__(self):
        self.comparisons = 0
        self.execution_time = 0
    
    def search(self, text, pattern):
        if not text or not pattern:
            return [], 0, 0
            
        self.comparisons = 0
        matches = []
        n = len(text)
        m = len(pattern)
        
        start_time = time.time()
        
        for i in range(n - m + 1):
            match = True
            j = 0
            
            while j < m and match:
                self.comparisons += 1
                if text[i + j] != pattern[j]:
                    match = False
                j += 1
                
            if match:
                matches.append(i)
                
        self.execution_time = (time.time() - start_time) * 1000  # Konversi ke milliseconds
        
        return matches, self.comparisons, self.execution_time
    
    def print_results(self, text, pattern, matches):
        print("\nHasil Pencarian Pattern Matching:")
        print("-" * 50)
        print(f"Pattern: {pattern}")
        print(f"Jumlah kecocokan ditemukan: {len(matches)}")
        print(f"Posisi kecocokan: {matches}")
        print(f"Jumlah perbandingan: {self.comparisons}")
        print(f"Waktu eksekusi: {self.execution_time:.4f} ms")
        

def main():
    matcher = BruteForceStringMatcher()
    
    text = ""
    pattern = ""
    
    matches, comparisons, execution_time = matcher.search(text, pattern)
    
    matcher.print_results(text, pattern, matches)

if __name__ == "__main__":
    main()
