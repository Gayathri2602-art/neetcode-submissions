
def perform_mydict(your_dict) ->dict:
  print(your_dict)
  print(your_dict["a"])
  print("d" in your_dict)
  your_dict["a"]=4
  print(your_dict)


your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}

perform_mydict(your_dict)