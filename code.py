class ThreeColorStacks:
    def __init__(self, N):
        self.N = N
        self.arr = [None] * N
        self.red_top = -1
        self.blue_top = N
        self.green_start = N // 2
        self.green_top = self.green_start - 1

    def _free_space_exists(self):
        if (self.red_top + 1) <= self.green_start and (self.green_top + 1) < self.blue_top:
            return True
        else:
            return False
        
    def _shift_green_left(self):
        if self.green_start == self.red_top + 1:
            return False
        for i in range(self.green_start, self.green_top + 1):
            self.arr[i - 1] = self.arr[i]
        self.arr[self.green_top] = None
        self.green_start -= 1
        self.green_top -= 1
        return True

    def _shift_green_right(self):
        if self.green_top + 1 == self.blue_top:
            return False
        for i in range(self.green_top, self.green_start - 1, -1):
            self.arr[i + 1] = self.arr[i]
        self.arr[self.green_start] = None
        self.green_start += 1
        self.green_top += 1
        return True

    def push_red(self, x):
        if self.red_top + 1 > self.green_start:
            if not self._shift_green_right():
                raise OverflowError("No space to push into Red Stack")
        self.red_top += 1
        self.arr[self.red_top] = x

    def pop_red(self):
        if self.red_top == -1:
            raise IndexError("Red stack is empty")
        x = self.arr[self.red_top]
        self.arr[self.red_top] = None
        self.red_top -= 1
        return x

    def peek_red(self):
        if self.red_top == -1:
            raise IndexError("Red stack is empty")
        return self.arr[self.red_top]

    def push_blue(self, x):
        if self.blue_top - 1 <= self.green_top:
            if not self._shift_green_left():
                raise OverflowError("No space to push into Blue stack")
        self.blue_top -= 1
        self.arr[self.blue_top] = x

    def pop_blue(self):
        if self.blue_top == self.N:
            raise IndexError("Blue stack is empty")
        x = self.arr[self.blue_top]
        self.arr[self.blue_top] = None
        self.blue_top += 1
        return x

    def peek_blue(self):
        if self.blue_top == self.N:
            raise IndexError("Blue stack is empty")
        return self.arr[self.blue_top]

    def push_green(self, x):
        if self.green_top + 1 >= self.blue_top:
            if not self._shift_green_left():
                raise OverflowError("No space to push into Green stack")
        self.green_top += 1
        self.arr[self.green_top] = x

    def pop_green(self):
        if self.green_top < self.green_start:
            raise IndexError("Green stack is empty")
        x = self.arr[self.green_top]
        self.arr[self.green_top] = None
        self.green_top -= 1
        return x

    def peek_green(self):
        if self.green_top < self.green_start:
            raise IndexError("Green stack is empty")
        return self.arr[self.green_top]

    def debug_print(self):
        print(self.arr)
        print("red_top =", self.red_top,
              "| green_start =", self.green_start,
              "| green_top =", self.green_top,
              "| blue_top =", self.blue_top)


if __name__ == "__main__":
    print()
    stacks = ThreeColorStacks(10)
    stacks.push_red(1)
    stacks.push_red(2)
    stacks.push_green(50)
    stacks.push_green(60)
    stacks.push_blue(100)
    stacks.push_blue(200)
    stacks.debug_print()
    print("pop_red:", stacks.pop_red())
    print("pop_green:", stacks.pop_green())
    print("pop_blue:", stacks.pop_blue())
    stacks.debug_print()
