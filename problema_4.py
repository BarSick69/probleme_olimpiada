import math
p_p=48
l_d=9
l_p=48/4
print("aflam latura patratului=perimetrul / 4 = ",l_p )
print("////////////////////////////////////////////// ")
a_p=l_p**2
print("aflam aria patratului dupa formula a^2="+f"{l_p}"+"^2 ="+f"{a_p}")
print("////////////////////////////////////////////// ")
print("aria dreptunghiului este egala cu a*b unde b =",l_d)
print("////////////////////////////////////////////// ")
print("a*"+f"{l_d}="+f"{a_p}"+"=>a="f"{a_p/l_d}")
a=a_p/l_d
print("////////////////////////////////////////////// ")
print("perimetrul dreptunghiului este egal cu 2(a+b)")
print("////////////////////////////////////////////// ")
raspuns=("gardul care imprejmureste acest lot are lungimea de "+f"2({l_d}+{a})= "+f"{2*(l_d+a)}"+" metri")
print(raspuns)