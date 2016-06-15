li = ["Larry", "Curly"]
print li.pop()
print getattr(li, "pop")
getattr(li, "append")("Moe")
print li
getattr({},"clear")
print ((),"pop")