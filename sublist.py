class sublist():
   def __init__(self, lst, start=0, end=None):
      """
      [start, end)
      """
      if end is None:
         end = len(lst)
      self.start = max(start, 0)
      self.end = min(end, len(lst))
      self.src = lst

   def __len__(self):
      return self.end - self.start

   def __getitem__(self, index):
      i = index + self.start
      if i >= self.start and i < self.end:
         return self.src.__getitem__(i)
      else:
         raise IndexError(index)

   def __repr__(self):
      return "[" + ",".join(repr(v) for i, v in enumerate(self.src) if i >= self.start and i < self.end) + "]"

   def __str__(self):
      return repr(self)

   def __eq__(self, value):
      if not isinstance(value, list) and not isinstance(value, sublist):
         return False
      if len(value) != len(self):
         return False
      for a, b in zip(self, value):
         if a != b:
            return False
      return True

   def __iter__(self):
      return SubListIter(self)

class SubListIter():
   def __init__(self, sublist):
      self.sublist = sublist
      self.index = 0
      self.end = len(sublist)

   def __next__(self):
      if self.index < self.end:
         self.index += 1
         return self.sublist[self.index - 1]
      else:
         raise StopIteration()


if __name__ == "__main__":
   assert sublist([]) == []
   assert sublist([1,2,3]) == [1,2,3]
   assert sublist([1,2], 0, 2) == [1,2]