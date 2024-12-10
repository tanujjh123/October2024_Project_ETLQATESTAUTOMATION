name = "Ramesh"
print("outside function " +name)

shopname = "abc store"
def profileGroceyShop():
    print("profile from groccessary and shop name is "+shopname)


onlinebusinessName = "Amazon"
def profileOnlineBusiness():
    print("profile from online business and business name is "+onlinebusinessName)
    print("profile from groccessary and shop name is " + shopname)


if __name__ =="__main__":
    profileGroceyShop()
    profileOnlineBusiness()
