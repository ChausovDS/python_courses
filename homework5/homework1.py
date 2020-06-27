import collections


org_num = int(input('сколько предприятий вы хотите ввести?'))
orgs = collections.defaultdict(list)
for i in range(org_num):
    org_name = input(f'введите название {i+1}-ой организации ')
    income = list(map(int, input('введите прибыль организации за 4 квартала через пробелы').split()))
    orgs[org_name] = income

mid_sum = sum([sum(i) for i in orgs.values()]) / org_num
print(mid_sum)
above_average = []
under_average = []
for org in orgs:
    if sum(orgs[org]) < mid_sum:
        under_average.append(org)
    else:
        above_average.append(org)
print(f'средняя годовая прибыль всех предприятий {mid_sum}')
orgs_to_out = ''
for i in above_average:
    orgs_to_out += i
print(f'предприятия, с прибылью выше среднего зачения: {orgs_to_out}')
orgs_to_out = ''
for i in under_average:
    orgs_to_out += i
print(f'предприятия, с прибылью ниже среднего зачения: {orgs_to_out}')
