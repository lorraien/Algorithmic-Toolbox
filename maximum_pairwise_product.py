# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    max_index1 = 0
    for i in range(len(numbers)):
        if numbers[i] > numbers[max_index1]:
            max_index1 = i
        else:
            continue

    if max_index1 == 0:
        max_index2 = 1
    else:
        max_index2 = 0
    for j in range(len(numbers)):
        if j != max_index1 and numbers[j] > numbers[max_index2]:
            max_index2 = j
        else:
            continue
    Product2 = numbers[max_index1] * numbers[max_index2]
    #print(max_index1)
    #print(max_index2)
    return Product2


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
