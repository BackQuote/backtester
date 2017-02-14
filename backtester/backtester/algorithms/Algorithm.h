#pragma once
#include <string>
#include <unordered_map>

using namespace std;

enum Action {
	buy = 0,
	sell = 1,
	nop = 2
};

class Algorithm {
public:
	Algorithm();
	~Algorithm();
	virtual Action processQuote(const double, const size_t) = 0;

protected:
	bool Algorithm::checkDayActive(size_t);
	unordered_map<string, double> algoParams;

private:
	const size_t marketOpenTime = 34'200'000; // milliseconds equivalent to 9h30
	const size_t marketCloseTime = 57'600'000; // milliseconds equivalent to 16h00
};