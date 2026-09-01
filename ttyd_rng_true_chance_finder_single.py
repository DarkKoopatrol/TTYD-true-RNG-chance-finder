mod = 10000
lowerBound = 8000
upperBound = 9999

rngValues = 2**15
workingVals = upperBound - lowerBound + 1
activations, remainder = divmod(rngValues, mod)
remainder -= lowerBound

extra = 0
if remainder > 0:
    if remainder < workingVals:
        extra = remainder
    else:
        activations += 1
numerator = workingVals * activations + extra
print(f"Chance: {numerator}/{rngValues}, {numerator / rngValues * 100}%")
