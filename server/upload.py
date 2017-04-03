from models import *
from sqlalchemy import update
from datetime import datetime, timedelta
import json


def save_models(simulation_results, backtest_id):
    params = simulation_results['params']
    results = simulation_results['results']
    profit_reset = simulation_results['profitReset']
    profit_rate_reset = simulation_results['profitRateReset']
    profit_no_reset = simulation_results['profitNoReset']
    profit_rate_no_reset = simulation_results['profitRateNoReset']
    profit_no_trading = simulation_results['profitNoTrading']
    profit_rate_no_trading = simulation_results['profitRateNoTrading']
    wallet_needed_for_reset = simulation_results['walletNeededForReset']
    ticker = simulation_results['ticker']

    # add simulation
    simulation = Simulation(json.dumps(params), profit_no_reset, profit_rate_no_reset, profit_reset, profit_rate_reset,
                            profit_no_trading, profit_rate_no_trading, wallet_needed_for_reset, backtest_id, str(ticker)
                            )
    db.session.add(simulation)
    db.session.commit()
    simulation_id = simulation.id

    # add results
    trade_models = []
    for day_result in results:
        day = db.session.query(Day).filter(Day.date == day_result['date']).first()
        result = day_result['result']
        trades = result['trades']

        result_model = Result(result['dailyProfitReset'], result['dailyProfitNoReset'], result['cumulativeProfitReset'],
                              result['cumulativeProfitNoReset'], day.id, simulation_id)
        db.session.add(result_model)
        db.session.commit()

        # add trades
        result_id = result_model.id
        for trade in trades:
            date = datetime.combine(day.date, datetime.min.time())
            date = date + timedelta(milliseconds=trade['timestamp'])
            time = datetime.strftime(date, "%Y-%m-%d %H:%M:%S.%f")
            trade_models.append(Trade(trade['price'], trade['quantityReset'], trade['quantityNoReset'], trade['action'],
                                      time, result_id))

        db.session.add_all(trade_models)
        db.session.commit()


def save_backtest(args):
    backtest = Backtest(args['params'], datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), False, args['algorithmId'])
    db.session.add(backtest)
    db.session.commit()

    for ticker in args['tickers']:
        db.session.execute(backtest_ticker.insert().values((backtest.id, ticker)))
    db.session.commit()

    return backtest.id


def backtest_completed(backtest_id, execution_time):
    db.session.query(Backtest).filter(Backtest.id == backtest_id).update(dict(success=True, execution_time=execution_time))
    db.session.commit()


def upload_template(args):
    template = Template(args)
    db.session.add(template)
    db.session.commit()
    return template