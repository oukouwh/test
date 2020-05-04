# 函数名调用用as定义别名，调用函数
import function_parent as fun

print(fun.sum_num(12))
# 211
fun.str_prt()
# This function is str_prt