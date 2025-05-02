import timeit
from algos.boyer_moore import boyer_moore_search
from algos.kmp import kmp_search
from algos.rabin_karp import rabin_karp_search 


def benchmark(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=10)

def compare_algorithms(algorithms, algorithms_results):
        with open("search_algo/data/стаття_1.txt", "r", encoding="utf-8") as f:
            text1 = f.read()
            
        with open("search_algo/data/стаття_2.txt", "r", encoding="utf-8") as f:
            text2 = f.read() 
        
        real_text1 = text1[100:150]
        real_text2 = text2[150:250]

        for name, func in algorithms.items():
            print(f"\n[{name}]")

            time = benchmark(func, text1, real_text1)
            algorithms_results[name] += time
            print("Article 1, real substring:   {:.6f} sec".format(time))

            time = benchmark(func, text1, real_text2)
            algorithms_results[name] += time
            print("Article 1, fake substring:   {:.6f} sec".format(time))

            time = benchmark(func, text2, real_text2)
            algorithms_results[name] += time
            print("Article 2, real substring:   {:.6f} sec".format(time))

            time = benchmark(func, text2, real_text1)
            algorithms_results[name] += time
            print("Article 2, fake substring:   {:.6f} sec".format(time))
        
        print("\n=== Загальні результати ===")
        for name, total_time in sorted(algorithms_results.items(), key=lambda item: item[1]):
            print(f"{name}: {total_time:.6f} sec")

if __name__ == "__main__": 

    algorithms = {
        "KMP": kmp_search,
        "Boyer-Moore": boyer_moore_search,
        "Rabin-Karp": rabin_karp_search
    }

    algorithms_results = {
        "KMP": 0,
        "Boyer-Moore": 0,
        "Rabin-Karp": 0  
    }

    compare_algorithms(algorithms, algorithms_results)
