def hanoi_tower(n, start, tmp, target):
    if n == 1:
        print(f"원반 {n} : {start} -> {target}")
        return 
    
    hanoi_tower(n - 1, start, target, tmp)
    print(f"원반 {n} : {start} -> {target}")
    hanoi_tower(n - 1, tmp, start , target)

if __name__ == "__main__":
    hanoi_tower(2, "A", "B", "C")