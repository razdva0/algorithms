from typing import Generator


def prime_numbers(n: int, start: int = 0) -> Generator[int, None, None]:
    a = list(range(n + 1))
    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            if a[i] > start:
                yield a[i]
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1


def main():
    for i in prime_numbers(100, start=50):
        print(i)


if __name__ == '__main__':
    main()
