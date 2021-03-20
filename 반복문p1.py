age = int(input("나이를 입력하세요 : "))
x = 0
while x <= age :
    if age % 2 == 0 :
        x = x + 2
        print(x)
    else :
        print(x)

print("메롱")
# if age % 2 == 0:
#     for i in range(2,age+2,2):
#         print(i)
# else :
#     for i in range(1,age+2,2):
#         print(i)
