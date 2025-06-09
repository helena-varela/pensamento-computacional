while True:
    N = int(input())
    if N == 0:
        break
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i >= j:
                print(f"{i - j + 1:>3}", end=" ")
            else:
                if j == N:
                    print(f"{j - i + 1:>3}", end="")
                else:
                    print(f"{j - i + 1:>3}", end=" ")
        print()
    print()
    