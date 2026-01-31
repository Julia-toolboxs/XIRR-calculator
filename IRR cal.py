#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IRR计算器
"""
import pandas as pd
cashflows = []  # 确保列表已初始化

a = input("input cash flows in order, separated by ',' ")
items = a.split(',')

for item in items:
    clean_item = item.strip()
    if not clean_item:
        continue
    try:
        num = float(clean_item)
        cashflows.append(num)
    except ValueError:
        print(f"⚠️ Warning: '{clean_item}' is not valid number，skipped")

print("cashflows:", cashflows)

def npv(cashflows, rate):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))

# 牛顿迭代法
rate = 0.10
for i in range(100):
    current_npv = npv(cashflows, rate)
    if abs(current_npv) < 0.01:
        break
    # 导数
    derivative = sum(-t * cf / (1 + rate) ** (t + 1) for t, cf in enumerate(cashflows) if t > 0)
    if abs(derivative) < 1e-10:
        break
    rate = rate - current_npv / derivative
    if rate < -0.9999 or rate > 10:
        rate = 0.10

# 结果输出
print("="*50)
print(f"Cashflows: {cashflows}")
print(f"IRR   : {rate*100:.2f}%")
print(f"NPV   : ¥{npv(cashflows, rate):.2f} (≈0 means Correct)")
print("="*50)