# TTYD-true-RNG-chance-finder
Finds the exact chance of a random event occurring based on the modulus of the random call and which random numbers result in the random event occurring. There's two versions of this, one for finding the chance of one outcome, and one for finding the chance of multiple outcomes of the same random call.

For the one outcome version, you'll have change mod, lowerBound, and upperBound to get the chance.

For the multiple outcomes version, you'll have to change mod and outcomes. Outcomes is an array of consecutive ranges that will produce different results, starting from 0.
