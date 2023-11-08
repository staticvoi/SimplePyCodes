def cal_area(b,h):
    print("__name__",__name__) #its main as we have main here
    return 10.5*b*h

# in IDLE- type __name__ and enter
# we get __main__
# __name__ is predefined var in python when we click run it is assigne dto __main__


if __name__=="__main__": #entry point
    print("i am in usemaindemo.py")
    a=cal_area(10,20)
    print("area=",a)