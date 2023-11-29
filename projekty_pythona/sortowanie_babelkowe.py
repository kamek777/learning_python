#Algorytm sortowania bąbelkowego
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Ostatnie i elementów są już na swoim miejscu, więc nie musimy ich porównywać
        for j in range(0, n-i-1):
            # Porównaj sąsiadujące elementy
            if arr[j] > arr[j+1]:
                # Zamień miejscami, jeśli są w złej kolejności
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Przykładowe użycie
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Tablica przed sortowaniem bąbelkowym:", arr)
    
    bubble_sort(arr)
    
    print("Tablica po sortowaniu bąbelkowym:", arr)

       
        
