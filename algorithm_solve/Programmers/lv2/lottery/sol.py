def find_best_number(n, arr):
  arr.sort()

  max_gap = 0
  best_number = 0

  if arr[0] - 1 > max_gap:
      max_gap = arr[0] - 1
      best_number = arr[0] - 1

  for i in range(len(arr) - 1):
      gap = (arr[i + 1] - arr[i]) // 2
      if gap > max_gap:
          max_gap = gap
          best_number = arr[i] + gap

  if n - arr[-1] > max_gap:
      max_gap = n - arr[-1]
      best_number = arr[-1] + 1

  return best_number


print(find_best_number(100, [40, 60, 80, 100, 20]))
print(find_best_number(7, [1, 5]))
print(find_best_number(11, [2,5,6,8]))