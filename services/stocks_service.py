# Logic for fetching and handling stock data

import yfinance as yf
from yfinance import exceptions as yf_exception

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
    """ Fetches stock data for the given list of tickers """
    
    data = {}
    
    try:
        CURRENT_EXCHANGE_RATE = yf.Ticker("USDEUR=X").history(period="1d")["Close"].iloc[-1].round(2)
    except(Exception):
        CURRENT_EXCHANGE_RATE = 1
    
    try:
        tickers = yf.Tickers(" ".join(ticker_list))  # Fetch data once for all tickers
    except yf_exception.YFinanceError:
        print("Could not fetch data for the given tickers")
        return data
    except Exception as e:
        print(f"An error occured: {e}")
        return data
    
    # Loop through the tickers and extract the data needed
    for ticker in ticker_list:
        try:
            stock = tickers.tickers[ticker]
        except KeyError:
            print(f"Could not fetch data for {ticker}")
            continue
        
        hist = stock.history(period="5d")
        
        closing_price = (hist["Close"].iloc[-1] * CURRENT_EXCHANGE_RATE).round(2)
        
        changePct = hist["Close"].pct_change().round(2).iloc[-1] * 100
        changeSymbol = "🔺" if changePct > 0 else " " if changePct == 0 else "🔻"
        
        sector = stock.info.get("sector", "No data available")
        
        # Get the recommendation of the stock
        try:
            recommendation = stock.recommendations.iloc[0]
            strongBuy, buy, hold, sell, strongSell = recommendation[
                ["strongBuy", "buy", "hold", "sell", "strongSell"]
            ]
            # Calculate the length of the bar chart
            strongBuy, buy, hold, sell, strongSell = calculateBarChartLength(
                strongBuy, buy, hold, sell, strongSell
            )
        except (IndexError, KeyError):
            strongBuy = buy = hold = sell = strongSell = 0
        
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

if __name__ == "__main__":
    print(get_stock_info(["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]))