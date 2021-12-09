def my_func(*args):
  args = list(args)
  biggest = args.pop(args.index(max(args)))
  return max(args) + biggest
print(my_func(11232, 2 ,4, 5))