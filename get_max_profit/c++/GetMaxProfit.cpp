#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>


void populateVector(std::vector<int>& p);

int main() {
    
    std::vector<int> prices;
    populateVector(prices);

    // for (int val : prices) {
    //     cout << val << endl;
    // }
        
    
    int minPrice = prices[0];
    int maximumProfit = prices[1] - prices[0];


    std::vector<int>::iterator it;
    for (it = ++prices.begin() ; it != prices.end() ; ++it) {
        int currentPrice = *it;
        
        // Check what the profit could be if we bought at min price
        // and sold at current price
        int potentialProfit = currentPrice - minPrice;
        
        // Check which profit is max
        maximumProfit = std::max(maximumProfit, potentialProfit);
        
        // Update min price
        minPrice = std::min(minPrice, currentPrice);
    
    }
    
    std::cout << maximumProfit << "\n";
    
    
    int i = 10;
    // std::cout << "Pre increment" << std::endl;
    // std::cout << ++i<< std::endl; //Pat: 11
    // std::cout << i << std::endl; // Pat: 11
    // i = 10;
    // std::cout << "Post increment" << std::endl;
    // std::cout << i++ << std::endl; //10
    // std::cout << i << std::endl; //11
    // i = 10;
    // std::cout << "Pre decrement" << std::endl;
    // std::cout << --i << std::endl; //9
    // std::cout << i << std::endl; //9
    // i = 10;
    // std::cout << "Post decrement" << std::endl;
    // std::cout << i-- << std::endl; //10
    // std::cout << i << std::endl; //9
    
    // i = 10;
    // std::cout << ++i + i++ << std::endl; // 11 + 12
    // std::cout << i << std::endl; // 23
    
    i = 10;
    std::cout << --i + i++ << std::endl;
    std::cout << i << std::endl;
    
    // i = 10;
    // std::cout << i-- + --i << std::endl;
    // std::cout << i << std::endl;
    
    
}

void populateVector(std::vector<int>& p) {
    p.push_back(12);
    p.push_back(11);
    p.push_back(10);
    p.push_back(9);
    p.push_back(8);
    p.push_back(7);
}