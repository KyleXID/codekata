# Day16.Week4(day2) prices라는 매일의 주식가격이 요소인 배열을 받습니다. 한번만 거래했을때, 가장 큰 이익을 반환하는 함수입니다.

def maxProfit(prices): 
  max_profit = 0
  
  for i in range(0,len(prices)-1):
    
    for j in range(i+1, len(prices)):
    
      if prices[i] >= prices[j]:
        continue
        
      elif prices[i] < prices[j]:
        maxpro = prices[j] - prices[i]
        max_profit = max(maxpro, max_profit)
        
  return max_profit
  
print(maxProfit([7,6,4,3,1]))


## 다른 방법

def maxProfit(prices):
  max_profit, min_price = 0, float('inf')

  for price in prices:
      min_price = min(min_price, price)
      profit = price - min_price
      max_profit = max(max_profit, profit)

  return max_profit
