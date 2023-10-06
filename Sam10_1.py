import time
def fibonacci():
    start = time.time()
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2)
    end = time.time()
    print("Временя работы программы ",(end-start) * 10**3, "миллисекунд")

if __name__ == "__main__":

    fibonacci()
