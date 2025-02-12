# Logic for fetching and handling stock data

import yfinance as yf

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
        
        recommondation = stock.recommendations.iloc[0][
            ["strongBuy", "buy", "hold", "sell", "strongSell"]
        ].to_string()
        
        data[ticker] = {
            "symbol": ticker,
            "closing_price": closing_price,
            "changePct": changePct,
            "changeSymbol": changeSymbol,
            "sector": sector,
            "recommondation": recommondation,
        } 
        
    return data
