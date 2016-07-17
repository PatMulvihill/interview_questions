// https://www.interviewcake.com/question/java/stock-price

//   int[] stockPricesYesterday = new int[]{10, 7, 5, 8, 11, 9};
//   getMaxProfit(stockPricesYesterday);
//   returns 6 (buying for $5 and selling for $11)

import java.util.Vector;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class GetMaxProfit {
    public static void main(String []args) {
        
        Integer[] prices = new Integer[]{11, 10, 9, 8, 7, 5};
        
        int maxProfit = Integer.MIN_VALUE;
        
        for (int i = 0; i < prices.length; ++i) {
            int beforePrice = prices[i];
            for (int j = i + 1; j < prices.length; ++j) {
                int afterPrice = prices[j];
                if (i < j) {
                    int profit = afterPrice - beforePrice;
                    maxProfit = Math.max(maxProfit, profit);
                }
            }
        }
        
        System.out.println(maxProfit);
        
    }
}


// This is the correct answer from interviewcake
/*
  public int getMaxProfit(int[] stockPricesYesterday) {

    // make sure we have at least 2 prices
    if (stockPricesYesterday.length < 2) {
        throw new IllegalArgumentException("Getting a profit requires at least 2 prices");
    }

    // we'll greedily update minPrice and maxProfit, so we initialize
    // them to the first price and the first possible profit
    int minPrice = stockPricesYesterday[0];
    int maxProfit = stockPricesYesterday[1] - stockPricesYesterday[0];

    // start at the second (index 1) time
    // we can't sell at the first time, since we must buy first,
    // and we can't buy and sell at the same time!
    // if we started at index 0, we'd try to buy /and/ sell at time 0.
    // this would give a profit of 0, which is a problem if our
    // maxProfit is supposed to be /negative/--we'd return 0!
    for (int i = 1; i < stockPricesYesterday.length; i++) {
        int currentPrice = stockPricesYesterday[i];

        // see what our profit would be if we bought at the
        // min price and sold at the current price
        int potentialProfit = currentPrice - minPrice;

        // update maxProfit if we can do better
        maxProfit = Math.max(maxProfit, potentialProfit);

        // update minPrice so it's always
        // the lowest price we've seen so far
        minPrice = Math.min(minPrice, currentPrice);
    }

    return maxProfit;
}
*/


