
# 基本语法
username: str = "zhangsan"

# 在函数中使用
def add(a: int, b: int) -> int:
    return a + b


def isAdult(age: int) -> bool:
    if age > 18:
        return True
    else:
        return False

# age: int = "18"