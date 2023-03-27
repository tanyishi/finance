from scipy import linalg
import numpy as np

stock_return = np.array([[0.003731,-0.001838,-0.003087,-0.024112],[0.021066,0.001842,-0.000344,0.011704],[-0.004854,-0.016544,-0.033391,-0.029563],[0.006098,-0.003738,0.007123,-0.01457]])
port_return = np.array([-0.0105654,0.0070534,-0.0256367,-0.0038289])
weight = linalg.solve(a=stock_return, b=port_return)
stock=np.array(['中国石油','工商银行','上汽集团','宝钢股份'])
for i in range(0,4):
    print(stock[i],round(weight[i],2))

def g(w):
    w1,w2,w3,w4 = w
    eq1 = 0.003731 * w1 - 0.001838 * w2 - 0.003087 * w3 - 0.024112 * w4 + 0.0105654  #第一个等于零的方程式
    eq2 = 0.021066 * w1 + 0.001842 * w2 - 0.000344 * w3 + 0.011704 * w4 - 0.0070534 #第二个等于零的方程式
    eq3 = -0.004854 * w1 - 0.016544 * w2 - 0.033391 * w3 - 0.029563 * w4 + 0.0256367 #第三个等于零的方程式
    eq4 = 0.006098 * w1 - 0.003738 * w2 + 0.007123 * w3 - 0.01457 * w4 + 0.0038289 #第四个等于零的方程式
    return [eq1, eq2, eq3, eq4]
import scipy.optimize as sco
results1 = sco.fsolve(g,[0.01,0.01,0.01,0.01])
results2 = sco.fsolve(g,[1,2,3,4])
print(results1)
print(results2)

P=np.array([590.01,5.29,26.67,6.50])  #输入股票价格
R=np.array([0.349032,0.155143,0.132796,0.055905])  #输入股票收益率
b=np.array([1.64,1.41,1.21,1.06])  #输入股票贝塔值

def f(w):  #定义求最优值的函数
    w=np.array(w)
    return -np.sum(R*w)

cons= ({'type':'eq','fun':lambda w:np.sum(w)-1},{'type':'ineq','fun':lambda w: 1.4-np.sum(w*b)})
bnds=((0,1),(0,1),(0,1),(0,1))
result=sco.minimize(f,[0.25,0.25,0.25,0.25],method='SLSQP',bounds=bnds,constraints=cons)
print(result)

print(result['x'].round(3))
#
print(-f(result['x']).round(3))

shares=1000000000*result['x']/P
shares=shares.round(0)

print('贵州茅台的股数：',shares[0])
print('工商银行的股数：',shares[1])
print('上汽集团的股数：',shares[2])
print('宝钢股份的股数：',shares[3])

cons_new= ({'type':'eq','fun':lambda w:np.sum(w)-1},{'type':'ineq','fun':lambda w: 1.2-np.sum(w*b)})

result_new=sco.minimize(f,[0.25,0.25,0.25,0.25],method='SLSQP',bounds=bnds,constraints=cons_new)
print(result_new['x'].round(3))

print(-f(result_new['x']).round(3))

shares_new=1000000000*result_new['x']/P
print('贵州茅台的股数：',shares_new[0].round(0))
print('工商银行的股数：',shares_new[1].round(0))
print('上汽集团的股数：',shares_new[2].round(0))
print('宝钢股份的股数：',shares_new[3].round(0))