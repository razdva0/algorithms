from typing import Generator


def knuth_morris_pratt(haystack: str, needle: str) -> Generator[int, None, None]:
    needle = list(needle)

    shifts = [1] * (len(needle) + 1)
    shift = 1
    for pos in range(len(needle)):
        while shift <= pos and needle[pos] != needle[pos - shift]:
            shift += shifts[pos - shift]
        shifts[pos + 1] = shift

    start_pos = 0
    match_len = 0
    for c in haystack:
        while match_len == len(needle) or match_len >= 0 and needle[match_len] != c:
            start_pos += shifts[match_len]
            match_len -= shifts[match_len]
        match_len += 1
        if match_len == len(needle):
            yield start_pos


def main():
    haystack = 'Hello, world! Hello, Python!'
    needle = 'ello'
    for x in knuth_morris_pratt(haystack, needle):
        print(x)


if __name__ == '__main__':
    main()
