import pandas as pd
import ace_tools as tools

# 初始化参数
initial_revenue = 10000  # 初始营业额
growth_rate_year1 = 0.10  # 第1年增长率
growth_rate_year2 = 0.08  # 第2年增长率
growth_rate_year3 = 0.05  # 第3年增长率

# 创建空列表存储每月营业额
revenue = []

# 计算第1年每月营业额
for month in range(12):
    if month == 0:
        revenue.append(initial_revenue)
    else:
        revenue.append(revenue[-1] * (1 + growth_rate_year1))

# 计算第2年每月营业额
for month in range(12):
    revenue.append(revenue[-1] * (1 + growth_rate_year2))

# 计算第3年每月营业额
for month in range(12):
    revenue.append(revenue[-1] * (1 + growth_rate_year3))

# 创建月份标签
months = [f"Year {i//12 + 1} Month {i%12 + 1}" for i in range(36)]

# 创建DataFrame
data = pd.DataFrame({
    'Month': months,
    'Revenue': revenue
})



tools.display_dataframe_to_user(name="Startup Revenue Simulation", dataframe=data)