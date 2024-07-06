#!/usr/bin/env python

def main():
    maxVal = 20
    sum = 0
    
    # 0, 1 2, 3, 4, 5, 6, 7, 8, 9.......20
    for i in range(0, maxVal+1):
        sum = sum + i
        print(sum, i)
    
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
