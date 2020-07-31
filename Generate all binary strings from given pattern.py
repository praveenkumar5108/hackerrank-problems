def _print(string, index): 
    if index == len(string): 
        print(''.join(string)) 
        return
  
    if string[index] == "?": 
  
        # replace '?' by '0' and recurse 
        string[index] = '0'
        _print(string, index + 1) 
  
        # replace '?' by '1' and recurse 
        string[index] = '1'
        _print(string, index + 1) 
  
        # NOTE: Need to backtrack as string 
        # is passed by reference to the 
        # function 
        string[index] = '?'
    else: 
        _print(string, index + 1) 
  
# Driver code 
if __name__ == "__main__": 
  
    string = "1??0"
    string = list(string) 
    _print(string, 0) 
