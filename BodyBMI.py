#计算身体的BMI值，并在国际和国内都BMI进行分类
height,weight=eval(input("请输入身高（米）和体重（公斤），并用逗号分隔:"))
bmi=weight/pow(height,2)
print("BMI的数值为{:.2f}".format(bmi))
who,nat="",""
if bmi<18.5:
    who,nat="偏瘦","偏瘦"
elif 18.5<=bmi<24:
    who,nat="正常","正常"
elif 24<=bmi<25:
    who,nat="正常","偏胖"
elif 25<=bmi<28:
    who,nat="偏胖","偏胖"
elif 28<=bmi<30:
    who,nat="偏胖","肥胖"
else :
    who,nat="肥胖","肥胖"
print("在国际中属于:{},国内属于:{}".format(who,nat))
