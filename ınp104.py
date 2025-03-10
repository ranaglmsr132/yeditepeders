def add(num1,num2):
  print(num1+num2)
  
def sub(num1,num2):
  print(num1-num2)
  
def mul(num1,num2):
  print(num1*num2)
  
def div(num1,num2):
  print(num1/num2)

while True:
 operator=input("İşlemi seçiniz: ")
 num1=float(input("Lütfen İlk Sayınızı Giriniz: "))
 num2=float(input("Lütfen İkinci Sayınızı Giriniz: "))
 

 if operator=="+":
   add(num1,num2)
 elif operator=="-":
   sub(num1,num2)
 elif operator=="*":
   mul(num1,num2)
 elif operator=="/":
   div(num1,num2)
 else:
   print("Tekrar Deneyin")




