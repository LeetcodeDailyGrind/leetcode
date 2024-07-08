class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink = numBottles
        while numBottles >= numExchange:
            exchange = numBottles // numExchange
            drink += exchange
            numBottles -= (exchange * numExchange)
            numBottles += exchange

        return drink