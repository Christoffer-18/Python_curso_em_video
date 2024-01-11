from time import sleep

def maior(*num):
    print("+=+"*20)
    print("Analisando valores passados", end=" ")
    for i in range(3):
        print(".", end="", flush=True)
        sleep(0.5)
    print("")
    if len(num) == 0:
        print(f"Foi informados {len(num)} números ao todo.")
        print(f"O maior valor informado foi 0.")
    else:
        for i in range(len(num)):
            print(f"{num[i]}", end=" ", flush=True)
            sleep(0.5)
            if i == 0:
                maiorn = num[i]
            elif maiorn < num[i]:
                maiorn = num[i]
        print(f"Foram informados {len(num)} números ao todo")
        print(f"O maior valor informado foi {maiorn}.")
    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()