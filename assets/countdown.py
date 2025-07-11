import time
def countdown(text,dur):
    for i in range(dur,0,-1):
        for j in range(4):
            print(f"{text} {i}{"."*j}    ", end="\r", flush=True)
            time.sleep(1/4)
    print(" "*50,end="\r",flush=True)