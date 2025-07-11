import time
def tprint(sample):
    for line in sample.splitlines():
        for i in range(len(line)):
            print(line[:i+1], end="\r", flush=True)
            time.sleep(0.01)
        print(line)
        time.sleep(0.5) 