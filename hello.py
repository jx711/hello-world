"""最小示例：打印问候语。"""


def greet(name: str = "World") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("jx711"))