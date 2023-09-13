# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/11 15:44
import numpy as np

'''
- 贝塔系数衡量个股相对于市场的风险程度。
- 贝塔系数大于1,表示个股的波动大于市场波动,具有较高风险。
- 贝塔系数等于1,表示个股的波动与市场一致。
- 贝塔系数小于1,表示个股的波动小于市场波动,风险较低。
- 贝塔系数为负,表示个股与市场变化方向相反。
'''
def calc_beta(stock_returns, market_returns):
    # 计算收益率的协方差
    cov = np.cov(stock_returns, market_returns)[0, 1]

    # 计算市场收益率的方差
    var = np.var(market_returns)

    # 计算贝塔系数
    beta = cov / var
    print(cov)
    print(var)
    return beta


# 股票收益率5日
stock_returns = [0.12, 0.05, -0.03, 0.08]
# 市场收益率5日
market_returns = [0.03, 0.01, -0.04, 0.06]

beta = calc_beta(stock_returns, market_returns)
print(beta)
