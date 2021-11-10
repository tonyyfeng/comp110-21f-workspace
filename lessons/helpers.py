"""Examples of functions imported elsewhere."""


THE_ANSWER: int = 42

def powerful(x: float, n: float) -> float:
    """Raise x to the power of n.""" 
    return x ** n

print(f"helpers.py: {__name__}")

if __name__ == "__main__":
    #python idiom: typicall you would call main here
    print(f"helpers.py: {__name__}")
    print("evaluated as a program")
else:
    #tyipcally common to not do anything if not main
    print("Evaluted as imported module")
