def calc_salary(per_hour, working, premium):
  return per_hour * working + premium

print(calc_salary(1000, 48, 20_000))