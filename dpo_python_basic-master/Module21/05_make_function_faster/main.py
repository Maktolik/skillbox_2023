def calculating_math_func(data, factorial={0: 1}):
    if data in factorial:
        result = factorial.get(data)
    else:
        for ind in range(max(factorial) + 1, data + 1):
            result = factorial.get(max(factorial))
            result *= ind
            factorial.update({ind: result})
        return calculating_math_func(data, factorial)

    result /= data ** 3
    result = result ** 10
    return result


number = int(input('Введите число: '))
res = calculating_math_func(number)
print(res)
