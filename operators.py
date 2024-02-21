input_days= 1000
print(f"years {input_days//365}")
remain_days = input_days%365
print(f"months {remain_days//30}")
remain_days= remain_days % 30
print(f"days {remain_days}")