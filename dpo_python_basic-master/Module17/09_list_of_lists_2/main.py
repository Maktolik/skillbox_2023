def main():
    nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

    un_scob = [lst_3 for lst_1 in nice_list for lst_2 in lst_1 for lst_3 in lst_2]
    print(un_scob)

main()