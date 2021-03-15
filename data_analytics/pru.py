import numpy as np

def main():
    count = 0

    for i in range(int(2e6)):
        rn = np.random.uniform()
        if rn < 1/1000:
            count += 1
    print(count)


if __name__ == '__main__':
    main()

