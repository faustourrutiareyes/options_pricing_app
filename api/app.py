from shiny import App, reactive, render, req, ui

# Own utils
from ticker_util import ticker_info_call
from price_simulators import black_scholes, simulate_stock_paths
from plotter import simulations_plot

import uvicorn

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_switch("use_ticker_switch", "Use actual asset data", False),
        
        # If using actual ticker data activate the following UI:
        ui.panel_conditional(
            "input.use_ticker_switch",
            ui.input_text("ticker", "Use a specific asset:", "^TWII"),  
            ui.output_text_verbatim("ticker_info_string"),  
        ),
        # Else
        ui.panel_conditional(
            "!input.use_ticker_switch",
            ui.input_numeric('sim_price', "Price of asset today", min = 100, max = 10000, step = 100, value = 700),
            ui.input_slider('sim_sigma', "Volatility (Sigma)", min=0, max=2, step=0.01, value=0.02),
        ),

        ui.input_radio_buttons(  
        "sim_call_or_put",  
        "Type of option",  
        {"call": "Call", "put": "Put"},  
        ),  
        ui.input_numeric('sim_strike', "Strike Price of Asset", min = 100, max = 30000, step = 100, value = 725), # Strike Price slider
        ui.input_slider('sim_rate', "Risk Free Rate", min=0.001, max=0.10, step=0.001, value=0.015), # Risk Free Rate
        ui.input_slider('sim_time', "Time to exercise (in years)", min=1, max=10, step=1, value=2), # Time to exercise option
        
        ui.output_text("option_price_string", inline = True),
        
        ui.input_numeric("sim_numpaths", "Number of simulations", min = 5, max = 10000, value = 20, step = 1),
        width = "20%"
    ),
    ui.layout_columns(
        ui.output_plot("path_simulator_plot"),
    ),

    title = "Monte Carlo Stock Volatility Simulator using GBM",
    fillable = True
)

def server(input, output, session):
    
    ticker_info = reactive.value()
    
    @render.text()
    def ticker_info_string():
        try:
            ticker_price_volatility = ticker_info.get()
            ticker_price = str(round(ticker_price_volatility[0], 2))
            ticker_volatility = str(round(ticker_price_volatility[1], 2))
            return "Last Price: " + ticker_price + "\nVolatilty: " + ticker_volatility
        except:
            return "Ticker information not found"
        
    @render.text
    def option_price_string():
        
        if input.use_ticker_switch():
            ticker_price_volatility = ticker_info.get()
            S0 = ticker_price_volatility[0]
            sigma = ticker_price_volatility[1]
        else:
            S0 = input.sim_price()
            sigma = input.sim_sigma()
            
        K = input.sim_strike()
        T = input.sim_time()
        r = input.sim_rate()
        
        option_type = input.sim_call_or_put()
            
        expected_price = black_scholes(S0, K, T, r, sigma, option_type = option_type)
        return "Expected premium of option: " + str(round(expected_price, 2))
    
    @render.plot
    def path_simulator_plot():
        
        if input.use_ticker_switch():
            ticker_price_volatility = ticker_info.get()
            S0 = ticker_price_volatility[0]
            sigma = ticker_price_volatility[1]
        else:
            S0 = input.sim_price()
            sigma = input.sim_sigma()
            
        K = input.sim_strike()
        T = input.sim_time()
        r = input.sim_rate()
        
        num_paths = input.sim_numpaths()
            
        paths = simulate_stock_paths(S0, T, r, sigma, num_paths)

        return simulations_plot(paths, K)
    
    @reactive.effect
    def ticker_update_info():
        new_info = ticker_info_call(input.ticker())
        ticker_info.set(new_info)
        


app = App(app_ui, server)

if __name__ == "__main__":
    uvicorn.run("app:app")