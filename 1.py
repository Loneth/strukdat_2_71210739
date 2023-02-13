import timeit
import matplotlib.pyplot as plt

x_axis = list([])
y_axis = list([])
bilangan_prima = list([])
i = 2
for bilangan in range(1, 999):
    prima = True
    for x in range(2, i):
        if i % x == 0:
            prima = False

    if prima:
        # print(i, end=" ")
        bilangan_prima.append(i)
    i += 1


def prima_iteratif(n: int):
    # ga = [bilangan_prima[dae] for dae in range(n)]
    for dae in range(n):
        # print(dae, end=" ")
        bilangan_prima[dae]
        # bilangan_prima[dae]

    # i = 2
    # jumlah = 0
    # while jumlah < n:
    #     prima = True
    #     for x in range(2, i):
    #         if i % x == 0:
    #             prima = False
    #
    #     if prima:
    #         # print(i, end=" ")
    #         jumlah += 1
    #     i += 1


def prima_rekrusif(n: int) -> int:
    if n == 0:
        return 0
    else:
        # print(bilangan_prima[n], end=" ")
        bilangan_prima[n]
        # print(n)
        prima_rekrusif(n - 1)


# prima_iteratif(10)
# print("\n")
# prima_rekrusif(10 - 1)
#
# for daeyes in bilangan_prima:
#     print(daeyes, end=" ")
# for yes in range(10):
#     prima_iteratif(yes)

# prima_iteratif(10)
# print("\n")
#
# for dae in range(2, 10 + 1):
#     # print(prima_rekrusif(dae))
#     print(dae)

# for dae in range(1, 10):
#     print(prima_rekrusif(dae))

# print("Bilangan Prima dari Iterasi")
# for dae in range(1, 100 + 1):
#     start = timeit.default_timer()
#     prima_iteratif(dae)
#     end = timeit.default_timer()
#
#     print(f"n = {dae} {end - start}")
#
# print("Bilangan Prima dari Rekrusif")

print("Iteratif")
for bilangan in range(100):
    start = timeit.default_timer()
    prima_iteratif(bilangan)
    end = timeit.default_timer()
    selisih = end - start
    print(f"n = {bilangan + 1} {selisih}")
    x_axis.append(selisih)
    # print(bilangan)

print("\n")
# print(len(bilangan_prima))

print("Rekrusif")
for bilangan in range(100):
    start = timeit.default_timer()
    prima_rekrusif(bilangan)
    end = timeit.default_timer()
    selisih = end - start
    print(f"n = {bilangan + 1} {selisih}")
    y_axis.append(selisih)
    # print(bilangan)

# prima_iteratif(10)
# prima_rekrusif(100 - 1)

plt.title('Perbandingan Waktu')
plt.scatter(x_axis, y_axis, color="darkblue", marker='x', label='item 1')
plt.xlabel('Waktu Iteratif')
plt.ylabel('Waktu Rekrusif')
plt.grid(True)
plt.legend()
plt.show()
