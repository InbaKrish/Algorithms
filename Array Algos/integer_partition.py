def integer_partition(n):
    n = n+1
    part_mat = [[0]*n for _ in range(n)]

    for summandindex in range(0,n):
        part_mat[summandindex][0] = 1

    for summandindex in range(1,n):
        for sumindex in range(1,n):
            if sumindex<summandindex:
                part_mat[summandindex][sumindex] = part_mat[summandindex-1][sumindex]
            else:
                combo_without_summand = part_mat[summandindex-1][sumindex]
                combo_with_summand = part_mat[summandindex][sumindex-summandindex]

                part_mat[summandindex][sumindex] = combo_with_summand+combo_without_summand

    print(part_mat)
    return part_mat[n-1][n-1]

print(integer_partition(5))
