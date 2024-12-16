import time

def brute_force_pattern_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    start_time = time.time()  # Mulai pengukuran waktu

    for i in range(n - m + 1):

        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:  # Jika seluruh pola cocok
            matches.append(i)  # Simpan indeks kecocokan

    end_time = time.time()  # Akhiri pengukuran waktu
    elapsed_time = (end_time - start_time) * 1000  # Konversi ke milidetik

    # Format waktu dalam 0.0000 ms
    print(f"Waktu eksekusi: {elapsed_time:.4f} ms")
    return matches

# Contoh penggunaan
text = ""
pattern = ""
result = brute_force_pattern_search(text, pattern)

print("Indeks kecocokan:", result)
