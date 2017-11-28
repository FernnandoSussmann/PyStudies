def test1(x):
  def tstfunc(z): 
    y = lambda l: l + l
    print y(z) , "end"
  
  for i in x:
    tstfunc(i)
    
  error0 = lambda message: "IT'S A DISASTER " + ("Mild" if message == "mild" else "DOOM")
  print error0("doom")
  
  comp = lambda info: "Mild" if info == "mild" else "DOOM"
  
  error = lambda message: "IT'S A DISASTER " + comp(message)
  print error("mild")
  
  
def main():
  x = [1,2,3,4,5,6,7,8,9,10]
  test1(x)
  
main()