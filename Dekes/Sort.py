class BubbleSorter:
    def init(self, numbers):
        self.numbers = numbers

    def sort(self):
        n = len(self.numbers)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = self.numbers[j + 1], self.numbers[j]

        return self.numbers


nums = [5, 3, 8, 1, 2]
sorter = BubbleSorter(nums)
print("Результат пузырьковой сортировки:", sorter.sort())
class InsertionSorter:
    def init(self, numbers):
        self.numbers = numbers

    def sort(self):
        for i in range(1, len(self.numbers)):
            key = self.numbers[i]
            j = i - 1

            while j >= 0 and key < self.numbers[j]:
                self.numbers[j + 1] = self.numbers[j]
                j -= 1

            self.numbers[j + 1] = key

        return self.numbers


nums = [9, 4, 1, 7, 3]
sorter = InsertionSorter(nums)
print("Результат сортировки вставками:", sorter.sort())
class HalfSorter:
    def init(self, numbers):
        self.numbers = numbers

    def sort_halves(self):
        mid = len(self.numbers) // 2

        first = sorted(self.numbers[:mid], reverse=True)
        second = sorted(self.numbers[mid:])

        return first + second


nums = [10, 4, 7, 1, 3, 9, 2, 8]
sorter = HalfSorter(nums)
print("Список после раздельной сортировки:", sorter.sort_halves())
class MergeSorter:
    def init(self, numbers):
        self.numbers = numbers

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(self):
        return self.merge_sort(self.numbers)


nums = [6, 2, 7, 3, 9, 1]
sorter = MergeSorter(nums)
print("Сортировка слиянием:", sorter.sort())