def loading_bar(current_val: int, max_val: int):
    # prints percentage on the same line over and over again like a loading bar
    # call from inside a loop every tieration
    # kinda neat
    print("%2.1f / 100" % (current_val / max_val * 100), end='\r')

if __name__ == "__main__":
    from time import sleep

    for x in range(100):
        loading_bar(x, 100)
        sleep(0.000000001)