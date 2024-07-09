class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        total_customers = len(customers)
        finish_time = 0
        for i in range(len(customers)):
            arrival_time = customers[i][0]
            prep_time = customers[i][1]

            if arrival_time >= finish_time:
                finish_time = arrival_time + prep_time
            else:
                finish_time = finish_time + prep_time
            
            total_waiting_time += finish_time - arrival_time

        return total_waiting_time / total_customers