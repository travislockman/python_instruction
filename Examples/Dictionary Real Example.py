# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

structure = [{'Arizona': 'Phoenix', 'California': 'Sacramento', 'Hawaii': 'Honolulu'},5000,6000,7000,['hat', 't-shirt',
                                                                                                      'jeans']]


print(structure[0])

account = [{'securitiesAccount': {'type': 'MARGIN', 'accountId': 'xxxxxxxxxx', 'roundTrips': 0, 'isDayTrader': False, 'isClosingOnlyRestricted': False, 'initialBalances':
                                       {'accruedInterest': 0.0, 'availableFundsNonMarginableTrade': 0.0,
                                        'bondValue': 0.0, 'buyingPower': 0.0, 'cashBalance': 0.0, 'cashAvailableForTrading': 0.0,
                                        'cashReceipts': 0.0, 'dayTradingBuyingPower': 0.0, 'dayTradingBuyingPowerCall': 0.0,
                                        'dayTradingEquityCall': 0.0, 'equity': 0.0, 'equityPercentage': 0.0, 'liquidationValue': 0.0,
                                        'longMarginValue': 0.0, 'longOptionMarketValue': 0.0, 'longStockValue': 0.0, 'maintenanceCall': 0.0,
                                        'maintenanceRequirement': 0.0, 'margin': 0.0, 'marginEquity': 0.0,
                                        'moneyMarketFund': 0.0, 'mutualFundValue': 0.0, 'regTCall': 0.0, 'shortMarginValue': 0.0,
                                        'shortOptionMarketValue': 0.0, 'shortStockValue': 0.0, 'totalCash': 0.0, 'isInCall': False,
                                        'pendingDeposits': 0.0, 'marginBalance': 0.0, 'shortBalance': 0.0, 'accountValue': 0.0},
                                        'currentBalances': {'accruedInterest': 0.0, 'cashBalance': 0.0, 'cashReceipts': 0.0, 'longOptionMarketValue': 0.0,
                                        'liquidationValue': 0.0, 'longMarketValue': 0.0, 'moneyMarketFund': 0.0,
                                        'savings': 0.0, 'shortMarketValue': 0.0, 'pendingDeposits': 0.0, 'availableFunds': 0.0,
                                        'availableFundsNonMarginableTrade': 0.0, 'buyingPower': 0.0, 'buyingPowerNonMarginableTrade': 0.0,
                                        'dayTradingBuyingPower': 0.0, 'equity': 0.0, 'equityPercentage': 0.0, 'longMarginValue': 0.0,
                                        'maintenanceCall': 0.0, 'maintenanceRequirement': 0.0, 'marginBalance': 0.0, 'regTCall': 0.0,
                                        'shortBalance': 0.0, 'shortMarginValue': 0.0, 'shortOptionMarketValue': 0.0, 'sma': 0.0, 'mutualFundValue': 0.0,
                                        'bondValue': 0.0}, 'projectedBalances': {'availableFunds': 0.0, 'availableFundsNonMarginableTrade': 0.0,
                                        'buyingPower': 0.0, 'dayTradingBuyingPower': 0.0, 'dayTradingBuyingPowerCall': 0.0, 'maintenanceCall': 0.0,
                                        'regTCall': 0.0, 'isInCall': False, 'stockBuyingPower': 0.0}}}]


print(account[0])
print(account[0]['securitiesAccount'])
print(account[0]['securitiesAccount']['projectedBalances'])
print(account[0]['securitiesAccount']['projectedBalances']['buyingPower'])





