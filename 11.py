#Множества- функция,которая может убрать из списка повторяющиеся элементы
# и эти элементы будут расположены в хаотичном порядке
#data = set('hello')
data = {9,5,7,4,3,5}

data.add(32)
data.update(['32',True,4,6])
data.remove(True)
data.pop()
#data.clear()

nums=[5,7,3,5,5]
new_nums=set(nums) #Удаляем повторения

#frozen set-это совместимость кортеж и множества

new_data = frozenset([5,7,4,'32',True,4,6,5,7,3,5])
#new_data.add - существует
print(new_data)