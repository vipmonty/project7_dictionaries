import sys
from time import perf_counter
from functools import lru_cache
# ===============================================================PART1:WEIGHT_ON_CACHELESS()=========================================================================================================

functions = 0


def weight_on_sides(r):
    global functions
    functions += 1
    person_weight = 200
    if r == 0:
        return (f"{0.0:.2f}")
    elif r == 1:
        return round(person_weight/2, 2)
    elif r == 2:
        x = weight_on_sides(r - 1)/2 + person_weight/r
        return round(x, 2)
    else:
        x = weight_on_sides(r - 1)/2 + person_weight/2
        return round(x, 2)


def weight_on_cacheless(r, c):
    global functions
    functions += 1
    person_weight = 200
    if r == 0 and c == 0:
        return weight_on_sides(r)
    elif c == 0 or c == r:
        return weight_on_sides(r)
    elif r == 2:
        topleft = weight_on_cacheless(r-1, c-1)/2 + person_weight/r
        topright = weight_on_cacheless(r-1, c)/2 + person_weight/r
        return round(topleft + topright, 2)
    elif r == 3:
        topleft = weight_on_cacheless(r-1, c-1)/2 + person_weight/2
        topright = weight_on_cacheless(r-1, c)/2 + person_weight/2
        return round(topleft + topright, 2)
    elif r == 4:
        topleft = weight_on_cacheless(r-1, c-1)/2 + person_weight/2
        topright = weight_on_cacheless(r-1, c)/2 + person_weight/2
        return round(topleft + topright, 2)
    elif r == 5:
        topleft = weight_on_cacheless(r-1, c-1)/2 + person_weight/2
        topright = weight_on_cacheless(r-1, c)/2 + person_weight/2
        return round(topleft + topright, 2)
    elif r == 6:
        topleft = weight_on_cacheless(r-1, c-1)/2 + person_weight/2
        topright = weight_on_cacheless(r-1, c)/2 + person_weight/2
        return round(topleft + topright, 2)
    else:
        topleft = weight_on_cacheless(r-1, c-1)/2 + person_weight/2
        topright = weight_on_cacheless(r-1, c)/2 + person_weight/2
        return round(topleft + topright, 2)


# print(weight_on_cacheless(0, 0))
# print(weight_on_cacheless(3, 1))
# ================================================================PART3:WEIGHT_ON_WITH_CACHING==================================================================================

cache = {}  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<USING HashMap ADT to change back just replace with {}
counter = -1
cache_counter = -1


@lru_cache(maxsize=None)
def weight_on_with_caching(r, c):

    global counter
    global cache_counter
    person_weight = 200
    keys = (r, c)
    counter += 1
    if keys in cache:
        return cache[keys]
    if r == 0 and c == 0:
        cache_counter += 1
        return weight_on_sides_with_caching(r)
    elif c == 0 or c == r:
        cache_counter += 1
        return weight_on_sides_with_caching(r)
    elif r == 2:
        cache_counter += 2
        topleft = weight_on_with_caching(r-1, c-1)/2 + person_weight/r
        topright = weight_on_with_caching(r-1, c)/2 + person_weight/r
        return round(topleft + topright, 2)
    else:
        cache_counter += 2
        topleft = weight_on_with_caching(r-1, c-1)/2 + person_weight/2
        topright = weight_on_with_caching(r-1, c)/2 + person_weight/2
        return round(topleft + topright, 2)


def weight_on_sides_with_caching(r, c=0):
    person_weight = 200
    global counter
    if r == 0:
        counter += 1
        return (f"{0.0:.2f}")
    elif r == 1:
        counter += 1
        return round(person_weight/2, 2)
    else:
        counter += 1
        x = weight_on_sides_with_caching(r - 1)/2 + person_weight/2
        return round(x, 2)


def main(arg):

    # ===============================================================PART2:CACHELESS================================================================================================

    start_timer = perf_counter()
    x = int(arg[1])
    for r in range(0, x):
        for c in range(0, r+1):
            print(weight_on_cacheless(r, c), end=" ")
        print("")
    end_timer = perf_counter()
    print(f"Elased time: {end_timer - start_timer} seconds")
    print(f"Number of function calls: {functions - 1}")


# ========================================================PART2:WRITE_OUTPUT_TO_CACHELESS.TXT===========================================================================

    with open("cacheless.txt", "w")as out_file:
        for r in range(0, int(sys.argv[1])):
            for c in range(0, r+1):
                out_file.write(
                    f"{weight_on_cacheless(r,c)}")
            out_file.write("\n")
        out_file.write(f"Elapsed time: { end_timer - start_timer} seconds\n")
        out_file.write(f"Number of function calls: {(functions//2)-1}\n")


# ==========================================================PART3:WITH CACHING OUTPUT====================================================================================

    timer_start = perf_counter()
    try:
        x = int(arg[1])
        for r in range(0, x):
            for c in range(0, r+1):
                print(weight_on_with_caching(r, c), end=" ")
                key = (r, c)
                cache[key] = weight_on_with_caching(r, c)
            print("")
    except:
        print("Please enter row number as integer.")
        print("usage from command line:<python3> <'pyramid.py'> <row number as integer>")

    timer_end = perf_counter()

    print("Elapsed time: ", timer_end - timer_start, "seconds")
    print(f"Number of function calls: {counter}")
    print(f"Number of cache hits: {cache_counter}")
    # print("This is the with_cache section============================================================================")
    text_counter = counter
    cache_count = cache_counter
    try:
        with open("with_caching.txt", "w")as out_file:
            for r in range(0, int(sys.argv[1])):
                for c in range(0, r+1):
                    out_file.write(f"{weight_on_with_caching(r,c)} ")
                out_file.write("\n")
            out_file.write(
                f"Elapsed time: { timer_end - timer_start} seconds\n")
            out_file.write(f"Number of function calls: {text_counter}\n")
            out_file.write(f"Number of cache hits: {cache_count}")
    except:
        print("Please enter row number as integer.")
        print("usage from command line:<python3> <'pyramid.py'> <row number as integer>")


if __name__ == "__main__":
    main(sys.argv)
