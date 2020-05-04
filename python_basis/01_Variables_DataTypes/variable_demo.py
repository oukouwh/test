
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 实验小案例
one, two, three = 6, 7, 8
print('    '*3+'Table统计')
print('|序号|' + ' |日期|          ' + '|商品名|' + '|数量|')
print('|1|   ' + '|2020/02/02|    ' + '|桌子|' + '%d |' % (one))
print('|2|   ' + '|2020/02/02|    ' + '|铅笔|' + '%d |' % (two))
print('|3|   ' + '|2020/02/02|    ' + '|橡皮|' + '%d |' % (three))
print('总计:%d+%d+%d=21' % (one, two,three))
