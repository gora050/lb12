class BigInteger:

    def __init__(self, initValue="0"):
        str_val = str(int(initValue)) # simple validator
        if str_val[0] == "-":
            self.negative = True
            str_val = str_val[1:]
        else:
            self.negative = False
        lst = list(map(int, str_val)) # chars to digits
        self.head = Digit(lst[-1])
        self.tail = self.head
        i = len(lst) - 2
        while i >= 0:
            temp = Digit(lst[i])
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
            i -= 1


    def __str__(self):
        return self.toString()

    def toString(self):
        end = 0
        s = ""
        tt = self.head
        while end != 1:
            s += str(tt.value)
            if tt.next is None:
                end = 1
            else:
                tt = tt.next
        return("-" * self.negative + s[::-1])

    def __floordiv__(self, other):
        return int(str(self)) // int(str(other))

    def __mul__(self,other):
        res = BigInteger()
        if self == BigInteger() or other == BigInteger():
            return BigInteger()
        A = BigInteger(str(self)[1:]) if str(self)[0] == "-" else BigInteger(str(self))
        B = BigInteger(str(other)[1:]) if str(other)[0] == "-" else BigInteger(str(other))
        while B > BigInteger():
            res = res + A
            B = B - BigInteger(1)
        if other.negative == self.negative:
            res.negative = False
        else:
            res.negative = True
        return res

    def __pow__(self,other):
        res = BigInteger(str(self))
        A = BigInteger(str(self))
        P = BigInteger(str(other)[1:]) if str(other)[0] == "-" else BigInteger(str(other))
        while P > BigInteger(1):
            P = P - BigInteger(1)
            res = res * A
        return res

    def __and__(self, other):
        return int(str(self)) & int(str(other))

    def __or__(self, other):
        return int(str(self)) | int(str(other))

    def __xor__(self, other):
        return int(str(self)) ^ int(str(other))

    def __lshift__(self, other):
        return self * (BigInteger(2) ** other)

    def __rshift__(self, other):
        return self // (BigInteger(2) ** other)

    def __add__(self, other):
        res = ""
        curr1 = self.head
        curr2 = other.head
        if self.negative != other.negative:
            return BigInteger(int(str(self)) + int(str(other)))
        else:
            ex = 0
            while True:
                if (curr1 == Digit() and curr2 == Digit() and ex == 0 and curr1.next is None and curr2.next is None):
                    return BigInteger("-" * self.negative + res if res != "" else 0)
                res = str(curr1.value + curr2.value + ex)[-1] + res
                ex = 1 if len(str(curr1.value + curr2.value + ex)) == 2 else 0
                curr1 = curr1.next if (curr1.next is not None) else Digit()
                curr2 = curr2.next if (curr2.next is not None) else Digit()

    def __sub__(self,other):
        curr2 = BigInteger(str(other)[1:]) if str(other)[0] == "-" else BigInteger("-"+str(other))
        return self + curr2

    def __lt__(self, other):
        A = self
        B = other
        if self.negative and not other.negative:
            return True
        elif not self.negative and other.negative:
            return False
        elif self.negative and other.negative:
            A, B = BigInteger(str(B)[1:]), BigInteger(str(A)[1:])
        if len(A) < len(B):
            return True
        elif len(A) > len(B):
            return False
        else:
            curr2, curr1 = B.tail, A.tail

            while curr1 is not None:
                if curr1.value < curr2.value:
                    return True
                elif curr1.value > curr2.value:
                    return False
                else:
                    curr1 = curr1.prev
                    curr2 = curr2.prev
        return False

    def __len__(self):
        slen = len(str(self))
        return slen-1 if self.negative else slen

    def __le__(self, other):
        return  self < other or self == other

    def __eq__(self, other):
        return True if str(self) == str(other) else False

    def __ne__(self, other):
        return not (self == other)

    def __ge__(self, other):
        return other <= self

    def __gt__(self, other):
        return  other < self


class Digit:
    def __init__(self, value="0"):
        self.value = int(value) # digit number < 10
        self.prev = None
        self.next = None

    def __eq__(self, other):
        return True if self.value == other.value else False
