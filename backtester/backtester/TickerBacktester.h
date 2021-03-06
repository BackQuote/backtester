#pragma once
#include "stdafx.h"
#include "algorithms/Algorithm.h"
#include "models/models.h"

class TickerBacktester {
public:
    TickerBacktester(const std::string &ticker, const std::string &backtesterRootDir, const std::string &algoName);
    ~TickerBacktester();
    void backtestAlgo(ctpl::thread_pool &tp, std::vector<std::unordered_map<std::string, double>> &paramCombos, std::mutex &m);

private:
    std::vector<Day> days;
    std::string ticker;
    std::string algoName;

    void loadUltimateFile(const std::string &ultimateFile);
    void split(const std::string &line, double lineInfo[], const char delimiter);
    void addQuotes(const double open, const double high, const double low, const double close, Day &day, std::size_t timestamp);
    void runSimulation(std::unordered_map<std::string, double> &params, std::vector<result_ns::Result> &results, double &lowestCumulativeProfitReset);
    std::unique_ptr<Algorithm> getAlgo(const std::unordered_map<std::string, double> &params);
    void simulateDay(double &dailyCashReset, double &dailyCashNoReset, result_ns::Result &result, std::unique_ptr<Algorithm> &algo, Day &day,
        std::unordered_map<std::string, double> &params);
    void handleAction(result_ns::Result &result, double &dailyCashReset, double &dailyCashNoReset, Action &action, Quote &quote, trade_ns::Trade &trade, 
        std::unique_ptr<Algorithm> &algo);
    void sendResults(std::unordered_map<std::string, double> &params, std::vector<result_ns::Result> &results, std::mutex &m, double &lowestCumulativeProfitReset);
};
