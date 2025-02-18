# Logic for fetching and handling stock data

import yfinance as yf

def calculateBarChartLength(
    strongBuy: int, buy: int, hold: int, sell: int, strongSell: int
):
    sum = strongBuy + buy + hold + sell + strongSell

    strongBuy = int((strongBuy / sum) * 100)
    buy = int((buy / sum) * 100)
    hold = int((hold / sum) * 100)
    sell = int((sell / sum) * 100)
    strongSell = int((strongSell / sum) * 100)

    # Check if any value is 0 and change it to 1
    strongBuy = strongBuy if strongBuy != 0 else 1
    buy = buy if buy != 0 else 1
    hold = hold if hold != 0 else 1
    sell = sell if sell != 0 else 1
    strongSell = strongSell if strongSell != 0 else 1

    return strongBuy, buy, hold, sell, strongSell

def get_stock_info(ticker_list):
    data = {}
    CURRENT_EXCHANGE_RATE = yf.Ticker("USDEUR=X").history(period="1d")["Close"].iloc[-1].round(2)
    
    for ticker in ticker_list:
        
        stock = yf.Ticker(ticker)
        
        hist = stock.history(period="5d")
        
        closing_price = (hist["Close"].iloc[-1]*CURRENT_EXCHANGE_RATE).round(2)
        
        changePct = hist["Close"].pct_change().round(2).iloc[-1] * 100
        changeSymbol = "🔺" if changePct > 0 else " " if changePct == 0 else "🔻"
        
        sector = stock.info.get("sector", "No data available")
        
        # Get the recommendation of the stock
        recommondation = stock.recommendations.iloc[0]
        strongBuy, buy, hold, sell, strongSell = recommondation[
            ["strongBuy", "buy", "hold", "sell", "strongSell"]
        ]
        # Calculate the length of the bar chart
        strongBuy, buy, hold, sell, strongSell = calculateBarChartLength(
            strongBuy, buy, hold, sell, strongSell
        )
        
        data[ticker] = {
            "symbol": ticker,
            "closing_price": closing_price,
            "changePct": changePct,
            "changeSymbol": changeSymbol,
            "sector": sector,
            "strongBuy": strongBuy,
            "buy": buy,
            "hold": hold,
            "sell": sell,
            "strongSell": strongSell,
        } 
        
    return data
