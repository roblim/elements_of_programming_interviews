def quicksort(arr)
  return arr if arr.length <= 1
  pivot = arr.pop
  left = []
  right = []
  arr.each { |el| el <= pivot ? left << el : right << el }
  quicksort(left) + [pivot] + quicksort(right)
end

