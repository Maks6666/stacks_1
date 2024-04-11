# 1
pages = []

pages.append("First one")
pages.append("Second one")
pages.append("Third one")

def return_to_prev():
    pages.pop()


pages.pop()
print(f"Current page is: {pages[-1]}")

