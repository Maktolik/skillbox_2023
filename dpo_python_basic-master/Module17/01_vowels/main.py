
def glas_find(text):
    glas = "аоиеёэыуюя"
    glass_on = [char for char in text if char in glas]
    return glass_on
def main():
    text = input("Введите текст: ")
    find_res = glas_find(text)
    print("Список гласных букв:", find_res)
    print("Длина списка:", len(find_res))

main()